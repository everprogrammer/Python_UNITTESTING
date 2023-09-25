from django.contrib import admin
from .models import Hash

# Register your models here.
class HashAdmin(admin.ModelAdmin):
    list_display = ('text', 'hash')

admin.site.register(Hash, HashAdmin)