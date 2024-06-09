from django.contrib import admin
from django.apps import apps
from contact import models

# Using decorator
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'category', 'show',
    ordering = '-id',
    list_filter = 'creation_date',
    search_fields = 'id', 'first_name', 'last_name',
    list_per_page = 10
    list_max_show_all = 100
    list_editable = 'first_name', 'last_name', 'show',
    list_display_links = 'id',


# Register all the models
models = apps.get_models()

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
