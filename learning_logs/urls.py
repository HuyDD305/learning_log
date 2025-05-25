"""Defind URL pattens for learning_logs app"""

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
    #Page for adding a new topic without going into admin site
    path('newtopic/', views.new_topic, name='new_topic'),
    #Page for adding a new entry for normal user
    path('new_entry/<int:topic_id>', views.new_entry, name='new_entry'),
    #Page for editing an entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),

]

