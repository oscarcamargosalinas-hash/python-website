from django import forms
from .models import Title, Notes

class TopicForm(forms.ModelForm):
    class Meta:
        model = Title
        fields = ['title']
        labels = {'title':''}

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['note']
        labels = {'note':''}
        widgets = {'note': forms.Textarea(attrs={'cols':80})}