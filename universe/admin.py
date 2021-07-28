from django.contrib import admin
from .models import Galaxy, StarSystem, Star, Planet

# Register your models here.

@admin.register(Galaxy)
class GalaxyAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "size_x",
        "size_y"
    ]
    fieldsets = (
        (None, {
            'fields': (
                ("name", "size_x", "size_y"),
            )
        })
    )
    
@admin.register(StarSystem)
class StarSystemAdmin(admin.ModelAdmin):
    list_display = [
        "name"
    ]


@admin.register(Star)
class StarAdmin(admin.ModelAdmin):
    list_display = [
        "name"
    ]


@admin.register(Planet)
class PlanetAdmin(admin.ModelAdmin):
    list_display = [
        "name"
    ]
