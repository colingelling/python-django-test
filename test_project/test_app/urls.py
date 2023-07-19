from django.urls import path

from . import views

app_name = 'django-app'  # Optional: Set the app name to avoid URL pattern conflicts

urlpatterns = [
    path('', views.home_view, name='home-view'),
    # Add more URL patterns as needed
]
