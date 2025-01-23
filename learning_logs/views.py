from django.shortcuts import render
from .models import Topic
# Create your views here.

def index(request):
    """página principal do learning log"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """Mostra todos os assuntos"""
    topics = Topic.objects.order_by('date_added') #query bd
    context = {'topics': topics} #create dictionary
    return render(request, 'learning_logs/topics.html', context)