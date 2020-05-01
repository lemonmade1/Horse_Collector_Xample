from django.contrib import admin
# import your models here
from .models import Horse, Feeding, Toy

# Register your models here
admin.site.register(Horse)
admin.site.register(Feeding)
admin.site.register(Toy)
