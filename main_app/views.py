from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Horse

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

class HorseList(ListView):
  model = Horse

  def get_queryset(self):
    return Horse.objects.all()

class HorseDetail(DetailView):
  model = Horse

class HorseCreate(CreateView):
  model = Horse
  fields = '__all__'  # edits all

class HorseUpdate(UpdateView):
  model = Horse
  fields = ['name', 'description', 'age']  # specific what to edit

class HorseDelete(DeleteView):
  model = Horse
  success_url = '/horses/'

# class HorsePix(DetailView):
#   model = Horse