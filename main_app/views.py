from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Horse, Toy
from .forms import FeedingForm

class HorseCreate(CreateView):
  model = Horse
  fields = ['name', 'breed', 'description', 'weight', 'history', 'age']

class HorseUpdate(UpdateView):
  model = Horse
  fields = ['breed', 'description', 'age']

class HorseDelete(DeleteView):
  model = Horse
  success_url = '/horses/'

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def horses_index(request):
  horses = Horse.objects.all()
  return render(request, 'horses/index.html', { 'horses': horses })

def horses_detail(request, horse_id):
  horse = Horse.objects.get(id=horse_id)

  # Get the toys the horse doesn't have
  toys_horse_doesnt_have = Toy.objects.exclude(id__in = horse.toys.all().values_list('id'))

  # Instantiate FeedingForm to be rendered in the template
  feeding_form = FeedingForm()
  return render(request, 'horses/detail.html', {

    # Pass the horse and feeding_form as context
    'horse': horse, 'feeding_form': feeding_form,

    # Add the toys to be displayed
    'toys': toys_horse_doesnt_have
  })

def add_feeding(request, horse_id):

	# create the ModelForm using the data in request.POST
  form = FeedingForm(request.POST)

  # validate the form
  if form.is_valid():
    
    # don't save the form to the db until it
    # has the horse_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.horse_id = horse_id
    new_feeding.save()
  return redirect('detail', horse_id=horse_id)

def assoc_toy(request, horse_id, toy_id):
  Horse.objects.get(id=horse_id).toys.add(toy_id)
  return redirect('detail', horse_id=horse_id)

def unassoc_toy(request, horse_id, toy_id):
  Horse.objects.get(id=horse_id).toys.remove(toy_id)
  return redirect('detail', horse_id=horse_id)

class ToyList(ListView):
  model = Toy

class ToyDetail(DetailView):
  model = Toy

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys/'




























# from django.shortcuts import render, redirect
# from django.views.generic import ListView, DetailView ##, HorsePix
# from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from .models import Horse, Toy
# from .forms import FeedingForm

# # Define the home view
# class HorseCreate(CreateView):
#   model = Horse
#   fields = ['name', 'breed', 'description', 'weight',
#   'history', 'age', 'toy']

# class HorseUpdate(UpdateView):
#   model = Horse
#   fields = ['name', 'description', 'weight',
#   'history', 'age', 'toy']

# class HorseDelete(DeleteView):
#   model = Horse
#   success_url = '/horses/'

# def home(request):
#   return render(request, 'home.html')

# def about(request):
#   return render(request, 'about.html')

# class HorseList(ListView):
#   model = Horse

#   def get_queryset(self):
#     return Horse.objects.all()

# class HorseDetail(DetailView):
#   model = Horse

# class HorseCreate(CreateView):
#   model = Horse
#   fields = '__all__'  # edits all

# class HorseUpdate(UpdateView):
#   model = Horse
#   fields = ['name', 'description', 'age']  # specific what to edit

# class HorseDelete(DeleteView):
#   model = Horse
#   success_url = '/horses/'





# def horses_index(request):
#   horses = Horse.objects.all()
#   return render(request, 'horses/index.html', { 'horses': horses })

# def horses_detail(request, horse_id):
#   horse = Horse.objects.get(id=horse_id)
#   toys_horse_doesnt_have = Toy.objects.exclude(id__in = horse.toys.all().values_list('id'))
#   feeding_form = FeedingForm()
#   return render(request, 'horses/detail.html', {
#     'horse': horse, 'feeding_form': feeding_form,
#     'toys': toys_horse_doesnt_have
#   })

# def add_feeding(request, horse_id):
#   form = FeedingForm(request.POST)
#   if form.is_valid():

#     # SAVE ONLY IF (horse_id) ASSIGNED
#     new_feeding = form.save(commit=False)
#     new_feeding.horse_id = horse_id
#     new_feeding.save()
#   return redirect('detail', horse_id=horse_id)

# def assoc_toy(request, horse_id, toy_id):
#   Horse.objects.get(id=horse_id).toys.add(toy_id)
#   return redirect('detail', horse_id=horse_id)

# def unassoc_toy(request, horse_id, toy_id):
#   Horse.objects.get(id=horse_id).toys.remove(toy_id)
#   return redirect('detail', horse_id=horse_id)

# class ToyList(ListView):
#   model = Toy

# class ToyDetail(DetailView):
#   model = Toy

# class ToyCreate(CreateView):
#   model = Toy
#   fields = '__all__'

# class ToyUpdate(UpdateView):
#   model = Toy
#   fields = ['name', 'color']

# class ToyDelete(DeleteView):
#   model = Toy
#   success_url = '/toys/'