from django.db import models


class Same_settings(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, db_index=True)
    position = models.PositiveSmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.name}'


# About
class About(Same_settings):
    ...


class Block_about(Same_settings):
    desc = models.TextField(max_length=1500, blank=True)
    photo = models.ImageField(upload_to='block_about/', blank=True)
    category = models.ForeignKey(About, on_delete=models.PROTECT, related_name='blocks_about')


# MENU
class Menu(Same_settings):
    ...


class DishCategory(Same_settings):
    # category = models.ForeignKey(Menu, on_delete=models.PROTECT, related_name='dishescat')
    ...

class Dish(Same_settings):
    ingredients = models.CharField(max_length=250)
    desc = models.TextField(max_length=500, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    photo = models.ImageField(upload_to='dishes/', blank=True)
    category = models.ForeignKey(DishCategory, on_delete=models.PROTECT, related_name='dishes')



# Events
class Events(Same_settings):
    ...


class Event(Same_settings):
    category = models.ForeignKey(Events, on_delete=models.PROTECT, related_name='events')
    desc = models.TextField(max_length=1500, blank=True)
    photo = models.ImageField(upload_to='event/', blank=True)


# Shefs
class Shefs(Same_settings):
    ...


class Shef(Same_settings):
    desc = models.TextField(max_length=1500, blank=True)
    photo = models.ImageField(upload_to='chef/', blank=True)
    job_title = models.CharField(max_length=50, unique=True)
    category = models.ForeignKey(Shefs, on_delete=models.PROTECT, related_name='shefs')