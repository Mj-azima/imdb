from django.contrib import admin
from .models import Film, Profile , Category


# Register your models here.


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    pass

@admin.register(Profile)
class FilmAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass