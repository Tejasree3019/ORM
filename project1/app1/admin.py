from django.contrib import admin
from . models import Movie,MovieAdmin

# Register your models here.
admin.site,register=(Movie,MovieAdmin)