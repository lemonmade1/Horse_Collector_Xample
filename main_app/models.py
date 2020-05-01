from django.db import models
from django.urls import reverse
from datetime import date

MEALS = (
  ('B', 'Breakfast'),
  ('L', 'Lunch'),
  ('D', 'Dinner')
)

class Toy(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('toys_detail', kwargs={'pk': self.id})

class Horse(models.Model):
  name = models.CharField(max_length=100)
  breed = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  weight = models.IntegerField()
  history = models.CharField(max_length=200)
  age = models.IntegerField()
  toys = models.ManyToManyField(Toy)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('detail', kwargs={ 'horse_id': self.id })

  def fed_for_today(self):
    return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)

class Feeding(models.Model):
  date = models.DateField('Feeding Date:')
  meal = models.CharField(
    max_length=1,
    choices=MEALS,
    default=MEALS[0][1]
  )

  horse = models.ForeignKey(Horse, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_meal_display()} on {self.date}"

  # CHANGE DEFAULT SORT (5,4,3,2,1)
  class Meta:
    ordering = ['-date']

