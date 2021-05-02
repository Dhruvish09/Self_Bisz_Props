from django.contrib import admin
from app.models import Contactus,reg,login,forgot,subscribe,team,slider,portfolio,category,cat_profile,client,sub_portfolio,Loan,ClientRequest,Businessdetail,Businessslide,demo
# Register your models here.

admin.site.register(reg)
admin.site.register(login)
admin.site.register(forgot)
admin.site.register(subscribe)
admin.site.register(Contactus)
admin.site.register(slider)
admin.site.register(team)
admin.site.register(portfolio)
admin.site.register(category)
# admin.site.register(sub)
admin.site.register(cat_profile)
admin.site.register(client)

admin.site.register(sub_portfolio)

admin.site.register(Loan)
admin.site.register(ClientRequest)
admin.site.register(Businessdetail)
admin.site.register(Businessslide)
admin.site.register(demo)



