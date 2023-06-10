from django.db import models
import cloudinary
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


class Room(models.Model):
    title = models.CharField(max_length=30)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name="room_details")
    price_per_night = models.DecimalField(max_digits=8, decimal_places=3)
    room_slug = models.SlugField()
    is_booked = models.BooleanField(default=False)
    capacity = models.IntegerField()
    room_size = models.CharField(max_length=5)
    featured = models.CharField(
       max_length=100,
       choices=[('Standard', 'Standard'), ('Delux', 'Delux'), ('Twin', 'Twin'), ('Premium', 'Premium')]
   )
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    

    def __str__(self):
        return self.title


class Category(models.Model):
    category_name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.category_name
