from django.shortcuts import render, redirect, HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User,auth
from django.contrib .auth import authenticate, login, logout
from django.contrib  import auth,messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password,check_password
from .models import Contactus,reg,team,portfolio,slider,client,portfolio,sub_portfolio,Loan,ClientRequest,Businessdetail,Businessslide,subscribe
from .form import Subscribeform,Regform,BusinessDetailform
from django.core.files.storage import FileSystemStorage
from django import template,forms

# (1) Start Index Page Area

def index(request):
    teams = team.get_all_tmdata()
    portfolios = portfolio.get_all_portdata()
    sub_portfolios = sub_portfolio.get_all_subportdata()
    sliders = slider.get_all_slidedata()
    clients = client.get_all_clntdata()
    return render(request, 'index.html',{'teams':teams,'portfolios':portfolios,'sub_portfolios':sub_portfolios,'sliders':sliders,'clients':clients})

def News(request):
    return render(request,'news.html')

def Sub_Portfolio(request):
    sub_portfolios = sub_portfolio.get_all_subportdata()
    return render(request,'Sub_Portfolio.html',{'sub_portfolios':sub_portfolios})

def loan(request):
    Loans = Loan.get_all_Loandata()
    return render(request,'loan.html',{'Loans':Loans})

def FAQ(request):
    return render(request,'FAQ.html')

def contact(request):
    all_data = Contactus.objects.all().order_by("-id")
    if request.method=="POST":
        nm = request.POST.get('name')
        em = request.POST.get('email')
        mb = request.POST.get('mobile')
        sub = request.POST.get('subject')
        msz = request.POST.get('message')
        
        data = Contactus(name=nm,email=em,mobile=mb,subject=sub,message=msz)
        data.save()
        return HttpResponse("Success! Thanx For Yor Response")
   
    return render(request,"contact.html")

def subs(request):
    teams = team.get_all_tmdata()
    portfolios = portfolio.get_all_portdata()
    sub_portfolios = sub_portfolio.get_all_subportdata()
    sliders = slider.get_all_slidedata()
    clients = client.get_all_clntdata()
    if request.method == "POST":
        email = request.POST.get('email')
        data = subscribe(email=email)
        data.save()
        return render(request,"index.html",{'teams':teams,'portfolios':portfolios,'sub_portfolios':sub_portfolios,'sliders':sliders,'clients':clients})
    return render(request,"index.html")

# End Index  Area   

# ........................................................
# ........................................................

# (2) Navbar Area start

def Activity(request):
    return render(request,'Activity.html')

def About(request):
    return render(request,'about.html')

def Services(request):
    return render(request,'services.html')

# End Navbar Area

# .........................................................
# .........................................................

#(3) Start Category Area:

def category(request):
    return render(request,'category.html')

def all_classifieds_cat(request):
    return render(request,'all-classifieds_cat.html')

def Technology(request):
    Businessslides = Businessslide.get_all_Bussliddata()
    Businessdetails = Businessdetail.get_all_busdetdata()
    return render(request,'Technology.html',{'Businessdetails':Businessdetails,'Businessslides':Businessslides})

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

# End category


# .....................................................................
# .....................................................................

#(4) Business Detail Page Area Start:-

def Business_Detail(request):
    Businessslides = Businessslide.get_all_Bussliddata()
    Businessdetails = Businessdetail.get_all_busdetdata()
    return render(request,'Business_Detail.html',{'Businessslides': Businessslides,'Businessdetails': Businessdetails})

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


# End Business Detail Page Ares

# .....................................................................
# .....................................................................


#(5) Login Registartion Forgot Start:-

# @login_required(login_url='final_log')

def final_reg(request):
    if request.method == "POST":
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        c_password = request.POST.get('c_password')
        birthdate = request.POST.get('birthdate')
        gender = request.POST.get('gender')
        phone_number = request.POST.get('phone_number')
        profile = request.POST.get('profile')
        photo =   request.FILES['photo'];
        hashedPassword = make_password(password=password)
        
        if password != c_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )
      
        Data = reg(photo=photo,email=email,username=username,birthdate=birthdate,gender=gender,phone_number=phone_number, password=hashedPassword,c_password=hashedPassword,profile=profile)
        Data.save()
        return render(request, 'Final_log.html',{'success':"user created successfully"})
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
#     if request.method == "POST":
#         print("something happen")
#         if reg.objects.filter(username=request.POST['username'],email=request.POST['email'],password=request.POST['password']).exists():
#             log = reg.objects.get(username=request.POST['username'],email=request.POST['email'],password=request.POST['password'])
#             return render(request,'Dashboard.html',{'log':log})
#         else:
#             return render(request,'Final_log.html',{'error':"Invalid Username or Password"})

#     return render(request,'Final_log.html')

def forgot(request):
    return render(request,'forgot.html')

def logoutuser(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("index")

# End Login Registartion Forgot 

# ...........................................................................
# ...........................................................................

#(6) Start Dashboard Area:-

def Dashboard(request):
    img = Businessslide.objects.filter().count()
    req_count = ClientRequest.objects.filter().count()
    byte = Businessdetail.objects.filter().count()
    ClientRequests = ClientRequest.get_all_cltreqdata()
    return render(request,'Dashboard.html',{'ClientRequests':ClientRequests,'byte':byte,'req_count':req_count,'img':img})

def Business_Detail_Form(request):
    req_count = ClientRequest.objects.filter().count()
    byte = Businessdetail.objects.filter().count()
    ClientRequests = ClientRequest.get_all_cltreqdata()
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
        return render(request,"Dashboard.html",{"status":res,"messages":all_data,'ClientRequests':ClientRequests,'byte':byte,'req_count':req_count})       
        # return HttpResponse("Best Of Luck for Your Business")
    return render(request,"Business_Detail_Form.html",{"messages":all_data})

def Buslide(request):
    if request.method == "POST":
        s = request.FILES['slide'];
        data = Businessslide(slide=s)
        data.save();
        data.clean()
        return redirect('/Dashboard')
    return render(request,"Dashboard.html")

    # ..............................................
        #(6.1) Dashboard Delete Operation

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
   
    
def delete_businessslide(request,id):
    if request.method == "POST":
        pi = Businessslide.objects.get(id=id)   
        pi.delete()
        return HttpResponseRedirect('/Dashboard')

    # ...................................................
        # (6.2) Dashboard Edit Operation

def Edit_Business_Detail_Form(request):
    Businessdetails = Businessdetail.get_all_busdetdata()
    return render(request,'Edit_Business_Detail_Form.html',{'Businessdetails': Businessdetails})

def Edit_Business_Slide_Form(request):
    Businessslides = Businessslide.get_all_Bussliddata()
    return render(request,'Edit_Business_Slide_Form.html',{'Businessslides': Businessslides})

def Edit_Profile(request):
    return render(request,'Edit_Profile.html')


# def edit(request,id):
#     detail = Businessdetail.objects.get(id=id)
#     if(request.method == "POST"):
#         form = BusinessDetailform(request.POST, instance=detail)
#         if(form.is_valid):
#             form.save()
#             return redirect("/")

#     else:
#         form = BusinessDetailform()
        
#     context = {
#         "BusinessDetailform":BusinessDetailform,
#         "Businessdetail":Businessdetail.objects.get(id=id),
#     }
    
#     return render(request,"edit.html",context) 


# End Dashboard Area
   
# .....................................................................
# .....................................................................
    

#(7)Start Client Dashboard Area:-

def Dashboard_C(request):
    req_count = ClientRequest.objects.filter().count()
    byte = Businessdetail.objects.filter().count()
    ClientRequests = ClientRequest.get_all_cltreqdata()
    return render(request,'Dashboard_C.html',{'ClientRequests':ClientRequests,'byte':byte,'req_count':req_count})


# Client Dashbaord Area End

# .....................................................................
# .....................................................................