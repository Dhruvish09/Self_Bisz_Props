#HR_

from django.shortcuts import render, redirect, HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib .auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password,check_password
from .models import registartion,team,portfolio,slider,category,cat_profile,client,portfolio,sub_portfolio,Loan,contact
from app.models import reg
from .form import Subscribeform,Regform


from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.core.mail import EmailMultiAlternatives
from django import template

# Create your views here.
# def index(request):
#     return render(request,'index.html')

def inner_page(request):
    return render(request,'inner-page.html')

def business_profile(request):
    return render(request,'business profile.html')

# ........................................................

# category

def categories(request):
    categorys = category.get_all_catdata()
    return render(request, 'category.html',{'categorys': categorys})

def category1(request):
    return render(request,'category1.html')

def all_classifieds_cat(request):
    return render(request,'all-classifieds_cat.html')

def Technology(request):
    cat_profiles = cat_profile.get_all_capdata()
    return render(request,'Technology.html',{'cat_profiles':cat_profiles})

def Vehical(request):
    return render(request,'vehical.html')

def Electronics_applices(request):
    return render(request,'electronics-appliances.html')

def Fashion(request):
    return render(request,'fashion.html')

def Furnitures(request):
    return render(request,'furnitures.html')

def Kids(request):
    return render(request,'kids.html')

def Pets(request):
    return render(request,'pets.html')

def Real_estate(request):
    return render(request,'real-estate.html')

def Business_Detail(request):
    return render(request,'Business_profile1.html')

# End category

# ........................................................

# Navbar start

def Activity(request):
    return render(request,'Activity.html')

def About(request):
    return render(request,'about.html')

def Services(request):
    return render(request,'services.html')

def Data(request):
    teams = team.get_all_tmdata();
    return render(request,'data.html',{'teams': teams})

# End Navbar

# .........................................................


def FAQ(request):
    return render(request,'FAQ.html')


# .....................................................................

# Login Registartion Forgot Start


# @login_required(login_url='final_log')
def index(request):
    teams = team.get_all_tmdata()
    portfolios = portfolio.get_all_portdata()
    sub_portfolios = sub_portfolio.get_all_subportdata()
    sliders = slider.get_all_slidedata()
    clients = client.get_all_clntdata()
    # name = request.user.username  
    return render(request, 'index.html',{'teams':teams,'portfolios':portfolios,'sub_portfolios':sub_portfolios,'sliders':sliders,'clients':clients})


# def final_reg(request):
#     if request.method == "GET":
#         return render(request,'Final_reg.html')
#     else:
#         try:
#             if request.method == "POST":
#                 email = request.POST.get('email')
#                 username = request.POST.get('username')
#                 password = request.POST.get('password')
#                 birthdate = request.POST.get('birthdate')
#                 gender = request.POST.get('gender')
#                 phone_number = request.POST.get('phone')
#                 profile = request.POST.get('profile')
#                 hashedPassword = make_password(password=password)
#                 user = (email=email,username=username,profile=profile,birthdate=birthdate,gender=gender,phone_number=phone_number, password=hashedPassword)
#                 user.save()
#                 return render(request, 'Final_log.html')
#         except:
#             return render(request,'Final_reg.html',{'error':"User Alredy Registered......."})
    
    # ency = make_password('12345')
    # print(ency)
    
    # decy = check_password('12345','pbkdf2_sha256$216000$a3P8F75Ie3ZB$T1x+naAXj/yifcwSEUhvwL4v6eznnvkt3egiFfiK1Ps=')
    # print(decy)
    
    # print(make_password('12345'))
    # print(check_password('123g45','pbkdf2_sha256$216000$a3P8F75Ie3ZB$T1x+naAXj/yifcwSEUhvwL4v6eznnvkt3egiFfiK1Ps='))
    
    
    # form = Regform()
    # if request.method == 'POST':
    #     form = Regform(request.POST)
    #     if form.is_valid():
    #         registartion.password = make_password('registartion.password')
    #         form.save()
    #         user = form.cleaned_data.get('username')
    #         messages.success(request, "account was created for" + user)
    #     return redirect('final_log')
    # context = {'form': form}
    # return render(request, 'final_reg.html', context)


def final_reg(request):
    if request.method == "GET":
        return render(request, 'Final_reg.html')
    else:
        try:
            if request.method == "POST":
                email = request.POST.get('email')
                username = request.POST.get('username')
                password = request.POST.get('password')
                birthdate = request.POST.get('birthdate')
                gender = request.POST.get('gender')
                phone_number = request.POST.get('phone')
                hashedPassword = make_password(password=password)
                user = reg(email=email,username=username,birthdate=birthdate,gender=gender,phone_number=phone_number, password=hashedPassword)
                user.save()
                return render(request, 'Final_log.html')
        except:
            return render(request, 'Final_reg.html', {'error': "User Already Registered..."})
        
      

def final_log(request):
    if request.method == 'GET':
        return render(request,"final_log.html")
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        userlog = reg.get_all_ptdata(email)
        print(userlog)
        error_message = None
        if userlog:
            flag = userlog
            #needs to check password here 
            flag = check_password(password,flag.password)
            #flag = authenticate(email=email , password = password)
            if flag:
                return redirect("about")
            else:
                error_message ="email or pass is wrong flag"   
        else:
            error_message = 'invalid email password outer flag'
        print(email,password)
        return render(request,'final_log.html',{'error' : error_message} )


# def final_forgot(request):
# return render(request,'final_forgot.html')
def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data)|Q(username=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    plaintext = template.loader.get_template('password_reset_email.txt')
                    htmltemp = template.loader.get_template('reset.html')
                    c = { 
                        "email":user.email,
					    'domain':'127.0.0.1:8000',
					    'site_name': 'Website',
					    "uid": urlsafe_base64_encode(force_bytes(user.pk)).decode(),
					    "user": user,
					    'token': default_token_generator.make_token(user),
					    'protocol': 'http',
         }
                    text_content = plaintext.render(c)
                    html_content = htmltemp.render(c)
                    try:
                        msg = EmailMultiAlternatives(subject, text_content, 'Website <admin@example.com>', [user.email], headers = {'Reply-To': 'admin@example.com'})
                        msg.attach_alternative(html_content, "text/html")
                        msg.send()
                        
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    messages.info(request, "Password reset instructions have been sent to the email address entered.")
                    return redirect ("index")
                
                password_reset_form = PasswordResetForm()
                return render(request=request, template_name="reset.html", context={"password_reset_form":password_reset_form})


def logoutuser(request):
    logout(request)
    return redirect('final_log')

# End Login Registartion Forgot 


# .....................................................................


# Start Sub_Portfolio

def Sub_Portfolio(request):
    sub_portfolios = sub_portfolio.get_all_subportdata()
    return render(request,'Sub_Portfolio.html',{'sub_portfolios':sub_portfolios})

# End Sub_Portfolio


def subscribe(request):
    form = Subscribeform()
    if request.method == 'POST':
        form = Subscribeform(request.POST)
        form.save()
        return redirect('index')
    context = {'form': form}
    return render(request, 'final_reg.html', context)

def profile(request):
    return render(request,'profile.html')

def loan(request):
    Loans = Loan.get_all_Loandata()
    return render(request,'loan.html',{'Loans':Loans})


def main_after(request):
    return render(request,'main_after.html')

def Dashboard(request):
    # name = request.user.username
    data = Client_Request.objects.all()
    return render(request,'Dashboard.html',{'data':data})


def Dashboard1(request):
    return render(request,'Dashboard1.html')


def Contactus(request):
    if request.method == "GET":
        return render(request,"contactform.html")
    if request.method == 'POST':
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        message = request.POST.get('message')
        cd = contact(name=name,subject=subject,email=email,message=message)
        cd.save()
        return render(request,"about.html")
    else:
        return HttpResponse("<h1>404 - Not Found</h1>")

def send(request):
    if request.method == 'POST':
        ID = request.POST['id']
        Email = request.POST['email']
        Client_Name = request.POST['client_name']
        Client_Request(ID = ID,email=Email,client_name=Client_Name).save()
        msg="Data Stored Successfully"
        return render(request,"index.html",{'msg':msg})
    else:
        return HttpResponse("<h1>404 - Not Found</h1>")
    
def delete(request):
    ID = request.GET['id']
    Client_Request.objects.filter(ID=ID).delete()
    return HttpResponseRedirect("show")

def edit(request):
    ID = request.GET['id']
    Email = client_name = "Not Available"
    for data in Client_Request.objects.filter(ID=ID):
        email = data.email
        client_name = client_name
    return render(request,"edit.html",{'ID':ID,'email':Email,'client_name':client_name})

def RecordEdited(request):
    
    if request.method == 'POST':
        ID = request.POST['id']
        Email = request.POST['email']
        Client_Name = request.POST['client_name']
        Client_Request.objects.filter(ID=ID).update(email=Email,client_name=Client_Name)
        return HttpResponseRedirect("show")
    else:
        return HttpResponse("<h1>404 - Not Found</h1>")