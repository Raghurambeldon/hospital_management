from django.contrib import admin
from .models import Doctor, Disease

@admin.register(Disease)
class DiseaseAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'rating', 'is_active')
    list_filter = ('specialization', 'is_active')
    search_fields = ('name',)
    filter_horizontal = ('diseases',)  # nice multi-select for ManyToMany
    readonly_fields = ()
