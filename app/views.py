from django.shortcuts import render, redirect, HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User,auth
from django.contrib .auth import authenticate, login, logout
from django.contrib  import auth,messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password,check_password
from .models import *
from .form import *
from django.core.files.storage import FileSystemStorage
from django import template,forms

# (1) Start Index Page Area

def index(request):
    teams = team.get_all_tmdata()
    portfolios = portfolio.get_all_portdata()
    sub_portfolios = sub_portfolio.get_all_subportdata()
    sliders = slider.get_all_slidedata()
    clients = client.get_all_clntdata()
    sub = subscribe.objects.filter().count()
    story = ShareStory.objects.filter().count()
    return render(request, 'index.html',{'teams':teams,'portfolios':portfolios,'sub_portfolios':sub_portfolios,'sliders':sliders,'clients':clients,'sub':sub,'story':story})

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

def story(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        story = request.POST.get('story')
        Data = ShareStory(name=name,email=email,story=story)
        Data.save()
        return redirect('/')
        # return render(request,"index.html")
    return render(request,"story.html")

def subs(request):
    if request.method == "POST":
        email = request.POST.get('email')
        data = subscribe(email=email)
        data.save()
        return redirect('/')
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
    # all_data = Businessdetail.objects.all().order_by("-id")
    if request.method == "POST":
        id = request.POST.get('id')
        Client_name=request.POST.get('Client_name')
        Client_email=request.POST.get('Client_email')
        Client_message=request.POST.get('Client_message')
        Client_Date=request.POST.get('Client_Date')
        Client_Mobile=request.POST.get('Client_Mobile')
        
        Data = ClientRequest(id=id,Client_name=Client_name,Client_email=Client_email,Client_message=Client_message,Client_Date=Client_Date,Client_Mobile=Client_Mobile)
        Data.save()
        messages.success(request, 'Dear {}, All The best for Your Request,we will notify you'.format(Client_name))
        return redirect('/Business_Detail')
    return render(request,'client_request.html')


# End Business Detail Page Ares

# .....................................................................
# .....................................................................



def Validateuser(user):
    error_message = None

    if len(user.username) < 5:
        error_message = "username must be long 5 or  morethan 5!!"

    elif user.isExists():
        error_message = "Email Address Already Registered..."

    elif len(user.phone_number) < 10:
        error_message = "Please enter 10 digit of your mobile number!!"
    elif len(user.password) < 6:
        error_message = "password Must be more than 8 character!!"
    
    elif user.password != user.c_password:
        error_message  =  "password and confirm_password does not match"
#(5) Login Registartion Forgot Start:-

# @login_required(login_url='final_log')

def final_reg(request):
    if request.method == 'GET':
        return render(request,"Final_reg.html")

    else:
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        c_password = request.POST.get('c_password')
        birthdate = request.POST.get('birthdate')
        gender = request.POST.get('gender')
        phone_number = request.POST.get('phone_number')
        profile = request.POST.get('profile')
        photo = request.FILES['photo']
        hashedPassword = make_password(password=password)      

        user = reg(email=email,
                    username=username,
                    birthdate=birthdate,
                    gender=gender,
                    phone_number=phone_number,
                    password=hashedPassword,
                    c_password=hashedPassword,
                    profile=profile,
                    photo=photo)

        value = {
            'username':username,
            'email':email,
            'birthdate':birthdate,
            'gender':gender,
            'phone_number':phone_number,
            'profile':profile,
            'photo':photo,
        }
        # error_message = Validateuser(user)
        error_message = None

        if len(username) < 5:
            error_message = "username must be long 5 or  morethan 5!!"

        elif user.isExists():
            error_message = "Email Address Already Registered..."

        elif len(phone_number) < 10:
            error_message = "Please enter 10 digit of your mobile number!!"
        
        elif not photo:
            error_message = "Please Select Your Photo"

        elif len(password) < 6:
            error_message = "password Must be more than 8 character!!"

        elif password != c_password:
            error_message  =  "password and confirm_password does not match"
        
        if not error_message:
            user.register()
            messages.success(request, 'Dear {}, Your Account is created Successfully'.format(username))
            return redirect('final_log')
        else:
            data = {
                'value' : value,
                'error': error_message
                }
            return render(request, 'Final_reg.html',data)
  

# def final_log(request):
#     if request.method =='POST':
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')

#         try:
#             user = reg.empAuth_objects.get(username=username,email=email,password=password)
#             if user is not None:
#                 print("Login Succesfful")
#                 return render(request,'Dashboard.html',{})
#             else:
#                 return redirect('/')
#         except Exception as identifier:
#             return redirect('/Dashboard')
#     else:
#         return render(request,'Final_log.html')  


def final_log(request):
    if request.method == "GET":
        return render(request,'Final_log.html')
    else:
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        client = reg.get_client_by_email(email)
        error_message = None
        if client:
            flag = check_password(password,client.password)
            if flag:
                return render(request,'Dashboard.html',{'username':username,'email':email})
                # return redirect('/Dashboard',{"username":username,"email":email})
            else:

                error_message = 'Email Or Password Invalid!!'
        else:
            error_message = 'Email Or Password Invalid!!'
        return render(request,'Final_log.html',{'error':error_message})

      
# def final_log(request):
#     if request.method == "GET":
#         return render(request,'final_log.html')
    
#     if request.method == "POST":
#         email = request.POST.get('email')
#         password = request.POST.get('password')
        
#         user = auth.authenticate(request,email=email, password=password)
#         if user is not None:
#             auth.login(request, user)
#             return redirect('Dashboard')
#         else:
#             messages.info(request, 'username or password is wrong')
#             return redirect('final_log')
#     context = {}
#     return render(request, 'Final_log.html',context)

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
        Business_Location = request.POST.get('Business_Location')
        Business_State = request.POST.get('Business_State')
        Business_Country = request.POST.get('Business_Country')
        Business_Address = request.POST.get('Business_Address')
        # Business_Photo = request.FILES.get('Business_Photo')
        Business_Photo = request.FILES['Business_Photo']

        data = Businessdetail(Business_Shortdetail=Business_Shortdetail,Business_Detail=Business_Detail,Business_Date=Business_Date,
                              Business_Brand=Business_Brand,Business_Brandweb=Business_Brandweb,
                              Business_Mobile=Business_Mobile,Business_Email=Business_Email,Business_Type=Business_Type,
                              Business_Turnover=Business_Turnover,Business_Marketplace=Business_Marketplace,Business_Features=Business_Features,
                              Business_Location=Business_Location,Business_State=Business_State,Business_Country=Business_Country,
                              Business_Address=Business_Address,Business_Photo=Business_Photo)
        data.save()
        messages.success(request,'Dear User, Thanks for Added Your Business of {}'.format(Business_Brand))
        # res = "Dear {} Thanks for Added Your Business".format(Business_Brand)
        # return render(request,"Dashboard.html",{"status":res,"messages":all_data,'ClientRequests':ClientRequests,'byte':byte,'req_count':req_count})       
        # return HttpResponse("Best Of Luck for Your Business")
        return redirect('/Dashboard')

    return render(request,"Business_Detail_Form.html")

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
        return redirect('/Dashboard')
    
def delete_businessdata(request,id):
    if request.method == "POST":
        pi = Businessdetail.objects.get(id=id)   
        pi.delete()
        return redirect('/Dashboard')
   
    
def delete_businessslide(request,id):
    if request.method == "POST":
        pi = Businessslide.objects.get(id=id)   
        pi.delete()
        return redirect('/Dashboard')

    # ...................................................
        # (6.2) Dashboard Edit Operation
        
def updatebuss(request,id):
    if request.method == "POST":
        pi = Businessdetail.objects.get(id=id)
        fm = BusinessDetailform(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Businessdetail.objects.get(id=id)
        fm = BusinessDetailform(instance=pi) 
        return render(request,'update_buss.html',{'form':fm})
    return redirect('/Dashboard')


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

def accountSettings(request):
	customer = request.user.customer
	form = CustomerForm(instance=customer)

	if request.method == 'POST':
		form = CustomerForm(request.POST, request.FILES,instance=customer)
		if form.is_valid():
			form.save()


	context = {'form':form}
	return render(request, 'accounts/account_settings.html', context)


def updatebus(request,id):
    if request.method == "POST":
        Business_Shortdetail = request.POST['Business_Shortdetail']
        Business_Detail = request.POST['Business_Detail']
        Business_Date = request.POST['Business_Date']
        Business_Brand = request.POST['Business_Brand']
        Business_Brandweb = request.POST['Business_Brandweb']
        Business_Mobile = request.POST['Business_Mobile']
        Business_Email = request.POST['Business_Email']
        Business_Type = request.POST['Business_Type']
        Business_Turnover = request.POST['Business_Turnover']
        Business_Marketplace = request.POST['Business_Marketplace']
        Business_Features = request.POST['Business_Features']
        Business_Location = request.POST['Business_Location']
        Business_State = request.POST['Business_State']
        Business_Country = request.POST['Business_Country']
        Business_Address = request.POST['Business_Address']
        Business_Photo = request.FILES['Business_Photo']
        Businessdetail.objects.filter(id=id).update(Business_Shortdetail=Business_Shortdetail,Business_Detail=Business_Detail,Business_Date=Business_Date,
                              Business_Brand=Business_Brand,Business_Brandweb=Business_Brandweb,
                              Business_Mobile=Business_Mobile,Business_Email=Business_Email,Business_Type=Business_Type,
                              Business_Turnover=Business_Turnover,Business_Marketplace=Business_Marketplace,Business_Features=Business_Features,
                              Business_Location=Business_Location,Business_State=Business_State,Business_Country=Business_Country,
                              Business_Address=Business_Address,Business_Photo=Business_Photo)
    dp = Businessdetail.objects.get(id=id)
    return render(request,'Update_Business_Detail_Form.html',{'dp':dp})

