from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import Http404

from .forms import TopicForm, EntryForm
from .models import Topic, Entry

# Create your views here.
def index(request):
    """The homepage for Learning Log"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """The page for topics"""
    topics = Topic.objects.order_by('date_added').filter(owner=request.user)
    context = {'topics': topics} # Pass data to template
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    """Show a single topic and all its entries"""
    topic = Topic.objects.get(id=topic_id)
    #Make sure the topic beongs to the current user
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic' : topic, 'entries' : entries} # Pass data to template
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    """Add a new topic for user"""
    if request.method != 'POST':
        #No data submitted; create a blank form.
        form = TopicForm()
    else:
        #POST data submitted; process data.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs:topics')

    #Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EntryForm()

    else:
        # POST data submitted; process data
        form = EntryForm(data=request.POST)

        if form.is_valid():
            new_entry = form.save(commit=False) #bao
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)

    #Display a blank or invalid form
    context = {'topic' : topic, 'form' : form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        #Initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry)
    else:
        #Post data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)
    context = {'entry' : entry, 'topic' : topic, 'form' : form}
    return render(request, 'learning_logs/edit_entry.html', context)


