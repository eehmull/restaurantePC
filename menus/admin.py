from django.contrib import admin
from django.contrib import admin
from .models import Plato, PlatoAdmin, Menu, MenuAdmin
# Register your models here.
admin.site.register(Plato, PlatoAdmin)
admin.site.register(Menu, MenuAdmin)
