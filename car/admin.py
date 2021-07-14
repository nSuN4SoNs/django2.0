from django.contrib import admin
from .models import Car, CarModel, Company, Colour, Rlsdate, Kind
# Register your models here.
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "vin_number",
        "car_model",
        "company",
        "colour",
        "rlsdate",
        "kind"
    ]
    fieldsets = (
        (None, {
            'fields': (
                ("name", "vin_number"),
            )
        }),
        ('Advanced options', {
            'fields': ("car_model", "company", "colour", "rlsdate", "kind"),
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

@admin.register(Rlsdate)
class RlsdateAdmin(admin.ModelAdmin):
    list_display = [
        "name"
    ]

@admin.register(Kind)
class KindAdmin(admin.ModelAdmin):
    list_display = [
        "name"
    ]