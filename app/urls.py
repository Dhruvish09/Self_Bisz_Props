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
   
    path('loan/',views.loan,name='loan'),
    
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
    path('password_reset_request/',views.password_reset_request,name='password_reset_request'),
    path('logoutuser/',views.logoutuser,name='logoutuser'),
    
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
    path('Sub_Portfolio/',views.Sub_Portfolio,name='Sub_Portfolio'),

    # End sub_category..........
    
    # End Category
    
    # ......................................................................
    path('send',views.send),
    path('delete',views.delete),
    # path('edit',views.edit),
    path('RecordEdited',views.RecordEdited),
    
    path('Edit_Profile',views.Edit_Profile,name="Edit_Profile")
  
    
]




