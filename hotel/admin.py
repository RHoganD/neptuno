from django.contrib import admin
from .models import Room, Category
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Room)
class RoomAdmin(SummernoteModelAdmin):


    list_display = ('title', 'room_slug', 'price_per_night','category',)
    search_fields = ['title', 'category']
    list_filter = ('is_booked', 'price_per_night', 'category', 'room_size',)
    prepopulated_fields = {'room_slug': ('title',)}
    summernote_fields = ('content',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)
    list_filter = ('category_name',)
    search_fields = ('category_name',)



