from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib .auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password,check_password
from .models import registartion,team,portfolio,slider,category,cat_profile,client,portfolio,tech_portfolio,auto_portfolio,book_portfolio,retail_portfolio,real_portfolio,furniture_portfolio
from .form import Subscribeform,Regform


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
    tech_portfolios = tech_portfolio.get_all_techportdata()
    auto_portfolios = auto_portfolio.get_all_autoportdata()
    book_portfolios = book_portfolio.get_all_bookportdata()
    retail_portfolios = retail_portfolio.get_all_retailportdata()
    real_portfolios = real_portfolio.get_all_realportdata()
    furniture_portfolios = furniture_portfolio.get_all_furniportdata()
    sliders = slider.get_all_slidedata()
    clients = client.get_all_clntdata()
    # name = request.user.username
    return render(request, 'index.html',{'teams':teams,'portfolios':portfolios,'tech_portfolios':tech_portfolios,'auto_portfolios':auto_portfolios,'book_portfolios':book_portfolios,'retail_portfolios':retail_portfolios,'furniture_portfolios':furniture_portfolios,'sliders':sliders,'clients':clients})


def final_reg(request):
    
    # ency = make_password('12345')
    # print(ency)
    
    # decy = check_password('12345','pbkdf2_sha256$216000$a3P8F75Ie3ZB$T1x+naAXj/yifcwSEUhvwL4v6eznnvkt3egiFfiK1Ps=')
    # print(decy)
    
    # print(make_password('12345'))
    # print(check_password('123g45','pbkdf2_sha256$216000$a3P8F75Ie3ZB$T1x+naAXj/yifcwSEUhvwL4v6eznnvkt3egiFfiK1Ps='))
    form = Regform()
    if request.method == 'POST':
        form = Regform(request.POST)
        if form.is_valid():
            registartion.password = make_password('registartion.password')
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "account was created for" + user)
        return redirect('final_log')
    context = {'form': form}
    return render(request, 'final_reg.html', context)


def final_log(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        registartion = authenticate(request, username=username, password=password)
        if registartion is not None:
            login(request, registartion)
            return redirect('Dashboard')
        else:
            messages.info(request, 'username or password in wrong')
    context = {}
    return render(request, 'final_log.html',context)


def final_forgot(request):
    return render(request,'final_forgot.html')


def logoutuser(request):
    logout(request)
    return redirect('final_log')

# End Login Registartion Forgot 


# .....................................................................


# Start Sub_Portfolio

def Tech_Portfolio(request):
    tech_portfolios = tech_portfolio.get_all_techportdata()
    return render(request,'Tech_Portfolio.html',{'tech_portfolios':tech_portfolios})

def Retail_Portfolio(request):
    retail_portfolios = retail_portfolio.get_all_retailportdata()
    return render(request,'Retail_Portfolio.html',{'retail_portfolios':retail_portfolios})

def Real_estate_Portfolio(request):
    real_portfolios = real_portfolio.get_all_realportdata()
    return render(request,'Real estate_Portfolio.html',{'real_portfolios':real_portfolios})

def Furniture_Portfolio(request):
    furniture_portfolios = furniture_portfolio.get_all_furniportdata()
    return render(request,'Furniture_Portfolio.html',{'furniture_portfolios':furniture_portfolios})

def Book_Portfolio(request):
    book_portfolios = book_portfolio.get_all_bookportdata()
    return render(request,'Book_Portfolio',{'book_portfolios':book_portfolios})

def Auto_Portfolio(request):
    auto_portfolios = auto_portfolio.get_all_autoportdata()
    return render(request,'Auto_Portfolio.html',{'auto_portfolios':auto_portfolios})

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



def main_after(request):
    return render(request,'main_after.html')

def Dashboard(request):
    # name = request.user.username
    return render(request,'Dashboard.html')


def Dashboard1(request):
    return render(request,'Dashboard1.html')

