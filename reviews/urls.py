# reviews/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('submit_review/<int:assignment_id>/', views.submit_review, name='submit_review'),
    path('analytics/', views.analytics_view, name='analytics'),
    path('download_analytics/', views.download_analytics, name='download_analytics'),
]