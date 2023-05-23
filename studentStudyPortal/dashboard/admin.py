from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Notes)#Notes Model [class name]
admin.site.register(Homework)#Homework Model [class name]
admin.site.register(Todo)#Todo Model [class name]
