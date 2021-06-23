from django.contrib import admin
from app.models import reg,slider,team,client,portfolio,sub_portfolio,Loan,Contactus,subscribe,ClientRequest,Businessdetail,Businessslide,ShareStory
# Register your models here.


class RegData(admin.ModelAdmin):
    list_display = ['username','gender','profile','phone_number','email']


class TeamData(admin.ModelAdmin):
    list_display = ['name','position','photo']
    ordering = ['name']


class ContactData(admin.ModelAdmin):
    list_display = ['name','subject','email','mobile','added_on']
    ordering = ['added_on']

class StoryData(admin.ModelAdmin):
    list_display = ['name','email','added_on']
    ordering = ['added_on']


class BusinessData(admin.ModelAdmin):
    list_display = ['Business_Brand','Business_Mobile','Business_Email','Business_Country','Business_Date']
    ordering = ['Business_Date']

class ClientData(admin.ModelAdmin):
    list_display = ['Client_name','Client_email','Client_Mobile','Client_Date']
    ordering = ['Client_Date']

class LoanData(admin.ModelAdmin):
    list_display = ['Bank_name','Loan_Type','Loan_Amount','Interest_Rate']
    ordering = ['Interest_Rate']


admin.site.register(reg,RegData)
admin.site.register(ShareStory,StoryData)
admin.site.register(slider)
admin.site.register(team,TeamData)
admin.site.register(client)
admin.site.register(portfolio)
admin.site.register(sub_portfolio)
admin.site.register(Loan,LoanData)
admin.site.register(Contactus,ContactData)
admin.site.register(subscribe)
admin.site.register(ClientRequest,ClientData)
admin.site.register(Businessdetail,BusinessData)
admin.site.register(Businessslide)




