from django.shortcuts import render
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView

def news_home(request):
    news = Articles.odjects.order_by('-date')
    return render(request, 'news/news_home.html', {'news' : news})

class NewDetailView(DetailView):
    model = Articles

def create(request):

      return render(request,'news/create.html')


