"""Defind URL pattens for learning_logs"""

from django.urls import path
# import the path function, which is needed
# when mapping URLs to views
from . import views

app_name = 'learning_logs' # Django automatically detects this!
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all topic
    path('topics/', views.topics, name='topics'),
    # Details page for a single topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),
]

