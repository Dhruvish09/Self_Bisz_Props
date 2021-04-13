from django.forms import ModelForm, fields
from phone_field import PhoneField
from django import forms
# from django .contrib.auth.models import User
from .models import registartion,login,forgot,contact,slider,subscribe,team,portfolio,category,cat_profile,client,sub_portfolio,Client_Request,Loan


# Start Reg , Log ,Forgot........................................................
class Regform(forms.ModelForm):
    # forms.ModelForm
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    # birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    phone_number = PhoneField()
    class Meta:
        model = registartion
        fields = ['email', 'username', 'password','gender','phone_number','profile']

class Logform(forms.ModelForm):
    class Meta:
        model = login
        fields = ['email', 'username', 'password']
        
class Forgotform(forms.ModelForm):
    class Meta:
        model = forgot
        fields = ['email']
        
# End Reg , Log ,Forgot........................................................



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
        model = contact
        fields = ['name','subject','email','message']

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




# Satrt Category.....................................................................

class Categoryform(forms.ModelForm):
    class meta:
        model = category
        fields = ['category','sub_category','photo']   
        
class cat_profileform(forms.ModelForm):
    class meta:
        model = cat_profile
        fields = ['Desc','Price','photo','city']  
        
# End Category.....................................................................           

class Clientrequestform(forms.ModelForm):
    class meta:
        model = Client_Request
        fields = ['id','email ','client_name','Desc'] 