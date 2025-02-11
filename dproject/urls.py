from django.urls import path
from . import views  # Make sure views is imported

app_name = 'dproject'

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('project/<int:project_id>/', views.project_detail, name='project_detail'),  # Correct view reference
    path('add/', views.add_project, name='add_project'),  # Add this line
]