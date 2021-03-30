from django.urls import path
from app import views

urlpatterns = [
    path('',views.index,name='index'),
    path('inner',views.inner_page,name='inner'),
    path('business_profile',views.business_profile,name='business_profile'),
    path('Business_Detail',views.Business_Detail,name='Business_Detail'),
    path('category/',views.category,name='category'),
    path('subcategories/',views.subcategories,name='subcategories'),
    path('all_classifieds_cat/',views.all_classifieds_cat,name='all_classifieds_cat'),
    path('about/',views.About,name='about'),
    path('services/',views.Services,name='services'),
    path('final_reg/',views.final_reg,name='final_reg'),
    path('final_log/',views.final_log,name='final_log'),
    path('final_forgot/',views.final_forgot,name='final_forgot'),
    # path('login/',views.login,name='login'),
    # path('reg/',views.reg,name='reg'),
    
    
    path('faq/',views.FAQ,name='faq'),
    path('Activity/',views.Activity,name='Activity'),
    

    path('header/',views.header,name='header'),
    path('footar/',views.footar,name='footar'),
    
    # subcategory
    path('Technology/',views.Technology,name='Technology'),
    path('Vehical/',views.Vehical,name='Vehical'),
    path('Electronics_applices/',views.Electronics_applices,name='Electronics_applices'),
    path('Fashion/',views.Fashion,name='Fashion'),
    path('Furnitures/',views.Furnitures,name='Furnitures'),
    path('Kids/',views.Kids,name='Kids'),
    path('Pets/',views.Pets,name='Pets'),
    path('Real_estate/',views.Real_estate,name='Real_estate'),
]

