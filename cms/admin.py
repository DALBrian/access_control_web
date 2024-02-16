from django.contrib import admin
from .models import *
admin.site.register(User)
admin.site.register(History)
admin.site.register(Door)
admin.site.register(Face)

# Register your models here.
