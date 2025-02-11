from django.contrib import admin
from .models import Project

# Customizing the admin display for Project
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')  # Columns to display in the admin list view
    search_fields = ('title', 'description')  # Add search functionality
    list_filter = ('created_at',)  # Filter by date

# Registering the model with custom admin
admin.site.register(Project, ProjectAdmin)