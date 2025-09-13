from django.db import models
from django.contrib import admin

# Create your models here.
class Movie(Models.Model):
    user_id=models.IntegerField(primary_key=True)
    movie_name=models.CharField(max_length=50)
    show_time=models.DateTimeField()
    seats=models.IntegerField()
    theatre_name=models.CharField(max_length=30)

class MovieAdmin(admin.ModelAdmin):
    list_display=('user_id','movie_name','show_time','seats','theatre_name')

