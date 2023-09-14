from django.contrib import admin
from .models import DishCategory, Dish, Menu, About, Block_about, Events, Event, Shefs, Shef
# Register your models here.


@admin.register(DishCategory)
class DishCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Block_about)
class Block_aboutAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Shef)
class ShefAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Shefs)
class ShefsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
