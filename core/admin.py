from django.contrib import admin
from .models import Note
admin.site.site_header = "The Notes Buddy Admin"

# Register your models here.
admin.site.register(Note)
