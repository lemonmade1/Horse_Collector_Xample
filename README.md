## username: lemonsterrell43@gmail.com
## password: cSjgp5LpW9HUQFk ( 'reddfoxxx' )

# Create an in-memory model (an instance of a Model) 

#### >>> c = Horse(name="Biscuit", breed='Sphinx',
#### >>> description='Evil looking cuddle monster. Hairless', age=2)
#### >>> c.__dict__
###### {..., 'id': None, 'name': 'Biscuit', 'breed': 'Sphinx',
###### 'description': 'Evil looking cuddle monster. Hairless', 'age': 2}

# Save it to the database:
### >>> c.save()
### >>> c.id
##### 1

# Update single attribute value by assigning new value and calling save()

#### >>> from main_app.models import Horse
#### >>> c = Horse.objects.first()
#### >>> c   
##### <Horse: Biscuit>

#### >>> c.name = 'Rubber Biscuit'
#### >>> c.save()
#### >>> c   
###### <Horse: Rubber Biscuit>

# Calls Horse.objects.all() and see a Horse object exists

### >>> Horse.objects.all()
##### <QuerySet [<Horse: Horse object (1)>]>

# FILTER (objects.filter()) query a Model's data that matches similar criteria 

### >>> Horse.objects.filter(name='Rubber Biscuit')
#### <QuerySet [<Horse: Rubber Biscuit>]>

# FILTER (objects.filter()) for all data with 'Bis' match

### >>> Horse.objects.filter(name__contains='Bis')
#### <QuerySet [<Horse: Rubber Biscuit>]>

### >>> Horse.objects.filter(age__lte=3)
#### <QuerySet [<Horse: Biscuit>]>

# An order_by method:

### >>> Horse.objects.order_by('name')

## Or in descending order:

### >>> Horse.objects.order_by('-age')

# Change User Password

### python3 manage.py changepassword <user_name>