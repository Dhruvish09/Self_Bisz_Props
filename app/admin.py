from django.contrib import admin
from app.models import registartion,login,forgot,subscribe,team,contact,slider,portfolio,category,cat_profile,client,sub_portfolio,Client_Request,Loan

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

admin.site.register(sub_portfolio)

admin.site.register(Loan)


admin.site.register(Client_Request)


