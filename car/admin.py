from django.contrib import admin
from .models import Car, CarModel, Company, Colour
# Register your models here.
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "vin_number",
        "car_model",
        "company",
        "colour"
    ]
    fieldsets = (
        (None, {
            'fields': (
                ("name", "vin_number"),
            )
        }),
        ('Advanced options', {
            'fields': ("car_model", "company", "colour"),
        }),
    )
    readonly_fields = [
        "company"
    ]

class CarInline(admin.StackedInline):
    model = Car

@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = [
        "name"
    ]
    inlines = [
        CarInline,
    ]

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = [
        "name"
    ]

@admin.register(Colour)
class ColourAdmin(admin.ModelAdmin):
    list_display = [
        "name"
    ]
