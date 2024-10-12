from django.contrib import admin
from .models import Client, ServiceProvider, Experience, Skill

admin.site.register(Client)
admin.site.register(ServiceProvider)
admin.site.register(Experience)
admin.site.register(Skill)

