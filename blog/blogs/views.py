from django.shortcuts import render, redirect
from .models import Title, Notes
from .forms import TopicForm, NotesForm
from django.contrib.auth.decorators import login_required
from django.http import Http404
# Create your views here.
def index(request):
    """Home page for Blogs"""
    return render(request, 'blogs/index.html')
@login_required
def titles(request):
    title = Title.objects.filter(owner=request.user).order_by('date_added')
    context = {'title':title}
    return render(request, 'blogs/titles.html', context)
@login_required
def note(request, title_id):
    title = Title.objects.get(id=title_id)
    check_topic_owner(request, title)
    note = title.notes_set.order_by('-date_added')
    context = {'note':note, 'title':title}
    return render(request, 'blogs/note.html', context)
def check_topic_owner(request, title):
    if title.owner != request.user:
        raise Http404
@login_required
def new_title(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_title = form.save(commit=False)
            new_title.owner = request.user
            new_title.save()
            return redirect('blogs:titles')
    context = {'form':form}
    return render(request, 'blogs/new_title.html', context)
@login_required
def new_notes(request, topic_id):
    title = Title.objects.get(id=topic_id)
    check_topic_owner(request, title)
    if request.method != 'POST':
        form = NotesForm()
    else:
        form = NotesForm(data=request.POST)
        if form.is_valid():
            new_notes = form.save(commit=False)
            new_notes.name = title
            new_notes.save()
            return redirect('blogs:note', title_id=topic_id)
    context = {'title':title, 'form':form}
    return render(request, 'blogs/new_notes.html', context)

@login_required
def edit_notes(request, note_id):
    note = Notes.objects.get(id=note_id)
    title = note.name
    check_topic_owner(request, title)
    if request.method != 'POST':
        form = NotesForm(instance=note)
    else:
        form = NotesForm(instance=note, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:note', title_id=title.id)
    context = {'title':title, 'form':form, 'note':note}
    return render(request, 'blogs/edit_notes.html', context)
