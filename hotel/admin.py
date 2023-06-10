from django.contrib import admin
from .models import Room, Category
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Room)
class RoomAdmin(SummernoteModelAdmin):


    list_display = ('title', 'room_slug', 'price_per_night','featured',)
    search_fields = ['title', 'featured']
    list_filter = ('featured', 'is_booked', 'price_per_night', 'capacity', 'room_size',)
    prepopulated_fields = {'room_slug': ('title',)}
    summernote_fields = ('content',)