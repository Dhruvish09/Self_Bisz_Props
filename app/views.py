from django.shortcuts import render, redirect, HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib .auth import authenticate, login, logout
from django.contrib  import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password,check_password
from .models import Contactus,reg,team,portfolio,slider,category,cat_profile,client,portfolio,sub_portfolio,Loan,ClientRequest,Businessdetail,Businessslide,subscribe
from .form import Subscribeform,Regform
from django import forms

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

def News(request):
    return render(request,'news.html')

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
    Businessslides = Businessslide.get_all_Bussliddata()
    Businessdetails = Businessdetail.get_all_busdetdata()
    return render(request,'Business_profile.html',{'Businessslides': Businessslides,'Businessdetails': Businessdetails})


# def Business_Detail_Form(request):
#     return render(request,'Business_Detail_Form.html')
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
    return render(request, 'index.html',{'teams':teams,'portfolios':portfolios,'sub_portfolios':sub_portfolios,'sliders':sliders,'clients':clients})

def final_reg(request):
    # if request.method == "GET":
    #     return render(request, 'Final_reg.html')
    # else:
    #     try:
    if request.method == "POST":
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        c_password = request.POST.get('c_password')
        birthdate = request.POST.get('birthdate')
        gender = request.POST.get('gender')
        phone_number = request.POST.get('phone_number')
        profile = request.POST.get('profile')
        hashedPassword = make_password(password=password)
        
        if password != c_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )
      
        Data = reg(email=email,username=username,birthdate=birthdate,gender=gender,phone_number=phone_number, password=hashedPassword,c_password=hashedPassword,profile=profile)
        Data.save()
        print("user created successfully")
        return render(request, 'Final_log.html')
                # return render(request, 'Dashboard.html')
        
        
                # return redirect('Dashboard')
        # except:
        print("something missing")
    return render(request, 'Final_reg.html', {'error': "User Already Registered..."})
        
def final_log(request):
    if request.method == "POST":
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = auth.authenticate(request,email=email, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('Dashboard')
        else:
            messages.info(request, 'username or password is wrong')
            return redirect('final_log')
    context = {}
    return render(request, 'Final_log.html',context)



# def final_log(request):
    # if request.method == 'GET':
    #     return render(request,"final_log.html")
    # else:
    #     email = request.POST.get('email')
    #     password = request.POST.get('password')
    #     userlog = reg.get_all_ptdata(email)
    #     print(userlog)
    #     error_message = None
    #     if userlog:
    #         flag = userlog
    #         #needs to check password here 
    #         flag = check_password(password,flag.password)
    #         #flag = authenticate(email=email , password = password)
    #         if flag:
    #             return redirect("about")
    #         else:
    #             error_message ="email or pass is wrong flag"   
    #     else:
    #         error_message = 'invalid email password outer flag'
    #     print(email,password)
    #     return render(request,'final_log.html',{'error' : error_message} )


# def final_forgot(request):
#     return render(request,'final_forgot.html')

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




def profile(request):
    return render(request,'profile.html')

def loan(request):
    Loans = Loan.get_all_Loandata()
    return render(request,'loan.html',{'Loans':Loans})


def main_after(request):
    return render(request,'main_after.html')

def Dashboard(request):
    # name = request.user.username
    req_count = ClientRequest.objects.filter().count()
    byte = Businessdetail.objects.filter().count()
    ClientRequests = ClientRequest.get_all_cltreqdata()
    return render(request,'Dashboard.html',{'ClientRequests':ClientRequests,'byte':byte,'req_count':req_count})

# def Client_request(request):
#     return render(request,'client_request.html')


def contact(request):
    all_data = Contactus.objects.all().order_by("-id")
    
    # if request.method == 'GET':
    #     return render(request,"contact.html")
    
    # else:
    if request.method=="POST":
        nm = request.POST.get('name')
        em = request.POST.get('email')
        mb = request.POST.get('mobile')
        sub = request.POST.get('subject')
        msz = request.POST.get('message')
        
        data = Contactus(name=nm,email=em,mobile=mb,subject=sub,message=msz)
        data.save()
        data.clean_fields()
        return HttpResponse("Success! Thanx For Yor Response")
   
    return render(request,"contact.html")

def subs(request):
    if request.method == "POST":
        email = request.POST.get('email')
        data = subscribe(email=email)
        data.save()
        res = "Dear {} Thanks for Connect With Us".format(email)
        return render(request,"index.html",{"status":res})
        # return HttpResponse("Thanx For Your Support")
    return render(request,"index.html")



def delete_clientdata(request,id):
    if request.method == "POST":
        pi = ClientRequest.objects.get(id=id)   
        pi.delete()
        return HttpResponseRedirect('/Dashboard')
    
def delete_businessdata(request,id):
    if request.method == "POST":
        pi = Businessdetail.objects.get(id=id)   
        pi.delete()
        return HttpResponseRedirect('/Dashboard')
    
def RecordEdited(request):
    
    if request.method == 'POST':
        ID = request.POST['id']
        Email = request.POST['email']
        Client_Name = request.POST['client_name']
        Client_Request.objects.filter(ID=ID).update(email=Email,client_name=Client_Name)
        return HttpResponseRedirect("show")
    else:
        return HttpResponse("<h1>404 - Not Found</h1>")
    
    
def Edit_Profile(request):
    
    
    # ID = request.GET['id']
    # Email = client_name = "Not Available"
    # for data in Client_Request.objects.filter(ID=ID):
    #     email = data.email
    #     client_name = client_name
    # return render(request,"edit.html",{'ID':ID,'email':Email,'client_name':client_name})
    return render(request,'Edit_Profile.html')

  
# Business_Shortdetail Business_Detail Business_Date Business_Brand Business_Brandweb Business_Mobile Business_Email 
# Business_Type Business_Turnover Business_Type Business_Marketplace  Business_Features  

def Business_Detail_Form(request):
    all_data = Businessdetail.objects.all().order_by("-id")
    if request.method=="POST":
        Business_Shortdetail = request.POST.get('Business_Shortdetail')
        Business_Detail = request.POST.get('Business_Detail')
        Business_Date = request.POST.get('Business_Date')
        Business_Brand = request.POST.get('Business_Brand')
        Business_Brandweb = request.POST.get('Business_Brandweb')
        Business_Mobile = request.POST.get('Business_Mobile')
        Business_Email = request.POST.get('Business_Email')
        Business_Type = request.POST.get('Business_Type')
        Business_Turnover = request.POST.get('Business_Turnover')
        Business_Marketplace = request.POST.get('Business_Marketplace')
        Business_Features = request.POST.get('Business_Features')


        data = Businessdetail(Business_Shortdetail=Business_Shortdetail,Business_Detail=Business_Detail,Business_Date=Business_Date,
                              Business_Brand=Business_Brand,Business_Brandweb=Business_Brandweb,
                              Business_Mobile=Business_Mobile,Business_Email=Business_Email,Business_Type=Business_Type,
                              Business_Turnover=Business_Turnover,Business_Marketplace=Business_Marketplace,Business_Features=Business_Features)
        data.save()
        res = "Dear {} Thanks for Added Your Business".format(Business_Brand)
        return render(request,"Dashboard.html",{"status":res,"messages":all_data})       
        # return HttpResponse("Best Of Luck for Your Business")
    return render(request,"Business_Detail_Form.html",{"messages":all_data})

def Edit_Business_Detail_Form(request):
    Businessdetails = Businessdetail.get_all_busdetdata()
    return render(request,'Edit_Business_Detail_Form.html',{'Businessdetails': Businessdetails})

def Client_request(request):
    all_data = Businessdetail.objects.all().order_by("-id")
    if request.method == "POST":
        id = request.POST.get('id')
        Client_name=request.POST.get('Client_name')
        Client_email=request.POST.get('Client_email')
        Client_message=request.POST.get('Client_message')
        Client_Date=request.POST.get('Client_Date')
        Client_Mobile=request.POST.get('Client_Mobile')
        
        Data = ClientRequest(id=id,Client_name=Client_name,Client_email=Client_email,Client_message=Client_message,Client_Date=Client_Date,Client_Mobile=Client_Mobile)
        Data.save()
        res = "Dear {} All The best for Your Request,we will notify you".format(Client_name)
        return render(request,"Business_profile.html",{"status":res,"messages":all_data})
    return render(request,'client_request.html')


# def subs(request):
#     if request.method == "POST":
#         email = request.POST.get('email')
#         data = subscribe(email=email)
#         data.save()
        # res = "Dear {} Thanks for Connect With Us".format(email)
        # return render(request,"index.html",{"status":res})
    #     return HttpResponse("Thanx For Your Support")
    # return render(request,"index.html")
    
def update_userdata(request,id):
    if request.method == "POST":
        pi= reg.objects.get(id=id)
        fm = Regform(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            print("successfully updated")
    else:
        pi = reg.objects.get(id=id)
        fm = Regform(instance=pi) 
        return render(request,'Edit_Profile.html',{'form':fm})
