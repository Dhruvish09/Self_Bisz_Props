from django.forms import ModelForm, fields
from phone_field import PhoneField
from django import forms
# from django .contrib.auth.models import User
from .models import reg,login,forgot,Contactus,slider,subscribe,team,portfolio,category,cat_profile,client,sub_portfolio,Loan,ClientRequest,Businessdetail,Businessslide
from django.core.mail import send_mail, get_connection
# Start Reg , Log ,Forgot........................................................
class Regform(forms.ModelForm):
    # forms.ModelForm
    # email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    # # birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    # password = forms.CharField(widget=forms.PasswordInput)
    # confirm_password = forms.CharField(widget=forms.PasswordInput)
    # phone_number = PhoneField()
    class Meta:
        model = reg
        fields = ['photo','email', 'username', 'password','c_password','gender','phone_number','profile','birthdate']

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
        model = Contactus
        fields = ['name','subject','email','mobile','message','added_on']


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

class ClientRequestform(forms.ModelForm):
    class meta:
        model = ClientRequest
        fields = ['id','Client_name','Client_email','Client_message','Client_Date','Client_Mobile']
        
class BusinessDetailform(forms.ModelForm):
    class meta:
        model = Businessdetail
        fields = ['Business_Shortdetail','Business_Detail','Business_Date','Business_Brandweb','Business_Brand','Business_Mobile','Business_Email','Business_Type','Business_Turnover','Business_Marketplace','Business_Features']

class Businessslideform(forms.ModelForm):
    class meta:
        model = Businessslide
        fields = ['slide']

