from django.db import models
from django.core.validators import MaxLengthValidator

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(validators=[MaxLengthValidator(160)])  # Apply the validator
    link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
