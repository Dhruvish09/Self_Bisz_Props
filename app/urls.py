from django.urls import path
from app import views

urlpatterns = [
    path('',views.index,name='index'),
    
    
    
    # .....................................................    
    
    # START
    
    path('Dashboard/',views.Dashboard,name='Dashboard'),
    path('Dashboard1/',views.Dashboard1,name='Dashboard1'),
    
    path('inner',views.inner_page,name='inner'),
    path('business_profile',views.business_profile,name='business_profile'),
    path('Business_Detail',views.Business_Detail,name='Business_Detail'),
   
     
    
    path('main_after/',views.main_after,name='main_after'),
    path('profile/',views.profile,name='profile'),
   
    path('Data/',views.Data,name='Data'),
    path('faq/',views.FAQ,name='faq'),
    
    # End
    
    # .....................................................   
    
        
    # Navigation Start
    
    path('about/',views.About,name='about'),
    path('services/',views.Services,name='services'), 
    path('Activity/',views.Activity,name='Activity'),
 
    # Navigation End
    
    
    # .....................................................
    
    
    # Log Reg Forgot Start
    
    path('final_reg/',views.final_reg,name='final_reg'),
    path('final_log/',views.final_log,name='final_log'),
    path('final_forgot/',views.final_forgot,name='final_forgot'),
    
    # Log Reg Forgot End
    
    
    
    # ...................................................................
       
    # category
    
    path('category/',views.categories,name='category'),
    path('category1/',views.category1,name='category1'),
    path('all_classifieds_cat/',views.all_classifieds_cat,name='all_classifieds_cat'),
    
    path('Technology/',views.Technology,name='Technology'),
    path('Vehical/',views.Vehical,name='Vehical'),
    path('Electronics_applices/',views.Electronics_applices,name='Electronics_applices'),
    path('Fashion/',views.Fashion,name='Fashion'),
    path('Furnitures/',views.Furnitures,name='Furnitures'),
    path('Kids/',views.Kids,name='Kids'),
    path('Pets/',views.Pets,name='Pets'),
    path('Real_estate/',views.Real_estate,name='Real_estate'),
    
    # sub_category..........
    path('Tech_Portfolio/',views.Tech_Portfolio,name='Tech_Portfolio'),
    path('Auto_Portfolio/',views.Auto_Portfolio,name='Auto_Portfolio'),
    path('Book_Portfolio/',views.Book_Portfolio,name='Book_Portfolio'),
    path('Furniture_Portfolio/',views.Furniture_Portfolio,name='Furniture_Portfolio'),
    path('Real_estate_Portfolio/',views.Real_estate_Portfolio,name='Real_estate_Portfolio'),
    path('Retail_Portfolio/',views.Retail_Portfolio,name='Retail_Portfolio'),
    # End sub_category..........
    
    # End Category
    
    # ......................................................................
]
