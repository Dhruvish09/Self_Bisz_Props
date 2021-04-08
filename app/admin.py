from django.contrib import admin
# <<<<<<< Updated upstream
from .models import registartion,login,forgot,subscribe,contact,team,slider
# >>>>>>> Stashed changes
# Register your models here.

admin.site.register(registartion)
admin.site.register(login)
admin.site.register(forgot)
admin.site.register(subscribe)
admin.site.register(contact)
# <<<<<<< Updated upstream
admin.site.register(slider)
# >>>>>>> Stashed changes
admin.site.register(team)

