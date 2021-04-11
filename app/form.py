from django.forms import ModelForm, fields
from phone_field import PhoneField
from django import forms
# from django .contrib.auth.models import User
from .models import registartion,login,forgot,contact,slider,subscribe,team,portfolio,category,cat_profile,client,tech_portfolio,auto_portfolio,real_portfolio,retail_portfolio,book_portfolio,furniture_portfolio


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
        fields = ['email', 'username', 'password', 'confirm_password','bday','gender','phone_number','profile']

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
        fields = ['photo']

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
        
# End Index....................................................................


       
# Start Sub_Portfolio...........................................................       
       
class Portfolioform(forms.ModelForm):
    class meta:
        model = portfolio
        fields = ['name','sub_name','photo']        

class Tech_Portfolioform(forms.ModelForm):
    class meta:
        model = tech_portfolio
        fields = ['name','photo']        

class Auto_Portfolioform(forms.ModelForm):
    class meta:
        model = auto_portfolio
        fields = ['name','photo']
               
class Retail_Portfolioform(forms.ModelForm):
    class meta:
        model = retail_portfolio
        fields = ['name','photo'] 
               
class Real_Portfolioform(forms.ModelForm):
        class meta:
            model = real_portfolio
            fields = ['name','photo']   
                 
class Book_Portfolioform(forms.ModelForm):
        class meta:
            model = book_portfolio
            fields = ['name','photo']        
                       
class Furniture_Portfolioform(forms.ModelForm):
        class meta:
            model = furniture_portfolio
            fields = ['name','photo']        

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
        
           