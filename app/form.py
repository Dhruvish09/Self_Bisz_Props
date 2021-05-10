from django.forms import ModelForm, fields
from phone_field import PhoneField
from django import forms
from .models import slider,team,portfolio,sub_portfolio,Contactus,subscribe,Loan,reg,Businessdetail,Businessslide,client,ClientRequest,ShareStory
from django.core.mail import send_mail, get_connection


# Start Area Reg .........................................................................

class Regform(forms.ModelForm):
    class Meta:
        model = reg
        fields = ['photo','email', 'username', 'password','c_password','gender','phone_number','profile','birthdate']

# End Area Reg ......................................................................


# Start Index.................................................................... 

class Slideform(forms.ModelForm):
    class meta:
        model = slider
        fields = ['photo']
        
class Clientform(forms.ModelForm):
    class meta:
        model = client
        fields = ['photo','Web']

class Contactform(forms.ModelForm):
    class meta:
        model = Contactus
        fields = ['name','subject','email','mobile','message','added_on']

class storyform(forms.ModelForm):
    class meta:
        model = ShareStory
        fields = ['name','email','story','added_on']


class Subscribeform(forms.ModelForm):
    class meta:
        model = subscribe
        fields = ['email']
        
class Teamform(forms.ModelForm):   
    class Meta:
        model = team
        fields = ['name','position','photo','twitter','facebook','instagram','linkedin']
        
class Loanform(forms.ModelForm):
    model = Loan
    fields = ['Bank_name','Loan_Type','Loan_Amount','Interest_Rate','Re_payment_Period','Address']
    
# End Index....................................................................


       
# Start Sub_Portfolio...........................................................       
       
class Portfolioform(forms.ModelForm):
    class meta:
        model = portfolio
        fields = ['name','sub_name','photo']        

class Sub_Portfolioform(forms.ModelForm):
    class meta:
        model = sub_portfolio
        fields = ['name','sub_name','photo']        

# End Sub_Portfolio...........................................................



# Start Business Area............................................................... 

# class BusinessDetailform(forms.ModelForm):
#     model = Businessdetail
#     fields = ['Business_Shortdetail','Business_Detail','Business_Date','Business_Brandweb','Business_Brand','Business_Mobile','Business_Email','Market_Type','Business_Type','Business_Turnover','Business_Marketplace','Business_Features',' Business_Address','Business_Country','Business_Location','Business_State','Business_Photo']

class BusinessDetailform(ModelForm):
  class Meta:
    model = Businessdetail
    fields = "__all__"



class Businessslideform(forms.ModelForm):
    class meta:
        model = Businessslide
        fields = ['slide']

# End Business Area............................................................... 



# Start Client Area..................................................................

class ClientRequestform(forms.ModelForm):
    class meta:
        model = ClientRequest
        fields = ['Client_name','Client_email','Client_message','Client_Date','Client_Mobile']

# End Client Area..................................................................