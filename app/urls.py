from django.urls import path
from app import views

urlpatterns = [

    # (1) Start Index Area:-

    path('',views.index,name='index'),
    path('story',views.story,name='story'),
    path('news',views.News,name='news'),
    path('Sub_Portfolio/',views.Sub_Portfolio,name='Sub_Portfolio'),
    path('contact',views.contact,name='contact'),
    path('subs',views.subs,name='subs'),
    path('loan',views.loan,name='loan'),
    path('faq',views.FAQ,name='faq'),

    # End Index Area


    # .....................................................   
    # .....................................................  

       
    # (2) Start Navigation Area:-
    
    path('about/',views.About,name='about'),
    path('services/',views.Services,name='services'), 
    path('Activity/',views.Activity,name='Activity'),
 
    # End Navigation Area
    
    # ..................................................... 
    # .....................................................

    # (3) Start Businessmen Dashboard Area:- 
    
    path('Dashboard/',views.Dashboard,name='Dashboard'),
    path('Business_Detail_Form',views.Business_Detail_Form,name='Business_Detail_Form'),
    path('edit_business',views.Edit_Business_Detail_Form,name='edit_business'),
    path('<int:id>/',views.updatebuss,name='updatebuss'),
    path('Buslide',views.Buslide,name='Buslide'), 
    path('editslide',views.Edit_Business_Slide_Form,name='editslide'),
    path('Client_request',views.Client_request,name='Client_request'),
    path('<int:id>/',views.updatebuss,name='updatebuss'),
    # ......................................................
            # (3.1)Start Delete Operation:
    path('delete/<int:id>/',views.delete_clientdata,name='deletedata'),
    path('deletebusiness/<int:id>/',views.delete_businessdata,name='deletebusiness'),
    path('deletebuslide/<int:id>/',views.delete_businessslide,name='deletebusslide'),
            # End Delete Operation
    # ........................................................

    # ........................................................
            #(3.2) Edit Operation Start:
    path('Edit_Profile',views.Edit_Profile,name="Edit_Profile"),
            # End Edit Operation:
    # ..........................................................


    # End Businessmen Dashboard Area:
    
    # .....................................................   
    # .....................................................  

    
    # (4) Start Clint Dashboard Area:

    path('Business_Detail',views.Business_Detail,name='Business_Detail'),
    path('cdash/',views.Dashboard_C,name='cdash'), 

    # Clent Dashboard Area End

 
    
    # .....................................................
    # .....................................................
    
    
    # (5) Start Log Reg Forgot:
    path('final_reg',views.final_reg,name='final_reg'),
    path('final_log',views.final_log,name='final_log'),
    path('forgot',views.forgot,name='forgot'),
    path('logoutuser/',views.logoutuser,name='logoutuser'),
    
    # Log Reg Forgot Area End
        
    # .........................................................
    # .........................................................
       

    # (6) Start Category Area:
    
    path('category/',views.category,name='category'),
    path('all_classifieds_cat/',views.all_classifieds_cat,name='all_classifieds_cat'),
    
    path('Technology/',views.Technology,name='Technology'),
    path('Vehical/',views.Vehical,name='Vehical'),
    path('Electronics_applices/',views.Electronics_applices,name='Electronics_applices'),
    path('Fashion/',views.Fashion,name='Fashion'),
    path('Furnitures/',views.Furnitures,name='Furnitures'),
    path('Kids/',views.Kids,name='Kids'),
    path('Pets/',views.Pets,name='Pets'),
    path('Real_estate/',views.Real_estate,name='Real_estate'),
    
    
    # Category Area End
    path('account/', views.accountSettings, name="account"),
    
    # ......................................................................
    # ......................................................................  
]




