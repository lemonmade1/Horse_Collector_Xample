## username: lemonsterrell43@gmail.com
## password: cSjgp5LpW9HUQFk ( 'reddfoxxx' )

# Create an in-memory model (an instance of a Model) 

#### >>> c = Cat(name="Biscuit", breed='Sphinx',
#### >>> description='Evil looking cuddle monster. Hairless', age=2)
#### >>> c.__dict__
###### {..., 'id': None, 'name': 'Biscuit', 'breed': 'Sphinx',
###### 'description': 'Evil looking cuddle monster. Hairless', 'age': 2}

# Save it to the database:
### >>> c.save()
### >>> c.id
##### 1

# Update single attribute value by assigning new value and calling save()

#### >>> from main_app.models import Cat
#### >>> c = Cat.objects.first()
#### >>> c   
##### <Cat: Biscuit>

#### >>> c.name = 'Rubber Biscuit'
#### >>> c.save()
#### >>> c   
###### <Cat: Rubber Biscuit>

# Calls Cat.objects.all() and see a Cat object exists

### >>> Cat.objects.all()
##### <QuerySet [<Cat: Cat object (1)>]>

# FILTER (objects.filter()) query a Model's data that matches similar criteria 

### >>> Cat.objects.filter(name='Rubber Biscuit')
#### <QuerySet [<Cat: Rubber Biscuit>]>

# FILTER (objects.filter()) for all data with 'Bis' match

### >>> Cat.objects.filter(name__contains='Bis')
#### <QuerySet [<Cat: Rubber Biscuit>]>

### >>> Cat.objects.filter(age__lte=3)
#### <QuerySet [<Cat: Biscuit>]>

# An order_by method:

### >>> Cat.objects.order_by('name')

## Or in descending order:

### >>> Cat.objects.order_by('-age')

# Change User Password

### python3 manage.py changepassword <user_name>