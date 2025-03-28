from django.shortcuts import render, redirect

from .forms import TopicFrom
from .models import Topic

# Create your views here.
def index(request):
    """The homepage for Learning Log"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """The page for topics"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics} # Pass data to template
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """Show a single topic and all its entries"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic' : topic, 'entries' : entries} # Pass data to template
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    """Add a new topic for user"""
    if request.method != 'POST':
        #No data submitted; create a blank form.
        form = TopicFrom()
    else:
        #POST data submitted; process data.
        form = TopicFrom(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs/topics')

    #Display a blank or invalid form.
    context = {'from': form}
    return render(request, 'learning_logs/new_topic.html', context)