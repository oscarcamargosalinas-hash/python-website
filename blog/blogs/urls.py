from django.urls import path
from . import views

app_name = 'blogs'
urlpatterns = [
    path('', views.index, name='index'),
    path('titles/', views.titles, name='titles'),
    path('titles/<int:title_id>', views.note, name='note'),
    path('new_title/', views.new_title, name='new_title'),
    path('new_notes/<int:topic_id>', views.new_notes, name='new_notes'),
    path('edit_notes/<int:note_id>/', views.edit_notes, name='edit_notes')
]