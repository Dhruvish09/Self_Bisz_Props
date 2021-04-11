from django.contrib import admin
from app.models import registartion,login,forgot,subscribe,team,contact,slider,portfolio,category,cat_profile,client,tech_portfolio,auto_portfolio,book_portfolio,retail_portfolio,real_portfolio,furniture_portfolio
# Register your models here.

admin.site.register(registartion)
admin.site.register(login)
admin.site.register(forgot)
admin.site.register(subscribe)
admin.site.register(contact)
admin.site.register(slider)
admin.site.register(team)
admin.site.register(portfolio)
admin.site.register(category)
# admin.site.register(sub)
admin.site.register(cat_profile)
admin.site.register(client)

admin.site.register(tech_portfolio)
admin.site.register(auto_portfolio)
admin.site.register(book_portfolio)
admin.site.register(retail_portfolio)
admin.site.register(real_portfolio)
admin.site.register(furniture_portfolio)

