from django.shortcuts import render
from django.http import HttpResponse
from .models import Horse

# # Note that parens are optional if not inheriting from another class
# class Horse:  
#   def __init__(self, name, breed, description, weight, history, age):
#     self.name = name
#     self.breed = breed
#     self.description = description
#     self.weight = weight
#     self.history = history
#     self.age = age

# horses = [
#   Horse(
#     'Peanut Butter', 
#     'Arabian',
#     'Compact body; wedge-shaped head; short back sloping',
#     '800 to 1,000 pounds',
#     'Oldest horse breed in the world', 
#     3
#   ),

#   Horse(
#     'Sasquash', 
#     'Thoroughbred', 
#     'Deep chest; lean body; long, flat muscles',
#     '1,000 to 1,300 pounds', 
#     'Most popular racing horse in North America',
#     0
#   ),

#   Horse(
#     'Spot', 
#     'Appaloosa', 
#     'Colorful coat pattern; mottled skin; striped hooves', 
#     '950 to 1,200 pounds',
#     'Great for herding, pleasure riding, long-distance',
#     7
#   ),

#   Horse(
#     'Chalk', 
#     'Morgan', 
#     'Small ears; expressive eyes; crested neck', 
#     '900 to 1,100 pounds',
#     'Popular driving and riding horse',
#     5
#   )
# ]

# Create your views here.
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')  

def about(request):
  return render(request, 'about.html')

def horses_index(request):
  horse = Horse.objects.all()
  return render(request, 'horses/index.html', {
    'horses': horses
  })

def horse_pix(request):
  horse = Horse.objects.all(id=horse_id)
  return render(request, 'horses/horses.html', {

  })

