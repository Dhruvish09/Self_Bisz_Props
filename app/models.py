from django.db import models
from phone_field import PhoneField
from django import forms
# from phonenumber_field.modelfields import PhoneNumberField
#   Start Index .........................................

class slider(models.Model):
    photo = models.ImageField(upload_to='media/slider/images') 
    
    @staticmethod
    def get_all_slidedata():
        return slider.objects.all()
    
class team(models.Model):
    name = models.CharField(max_length=30)
    position = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='media/team/images')
    twitter = models.URLField(max_length=250)
    facebook = models.URLField(max_length=250)
    instagram = models.URLField(max_length=250)
    linkedin = models.URLField(max_length=250)
    
    
    @staticmethod
    def get_all_tmdata():
        return team.objects.all()

    def __str__(self):
        return self.name

class client(models.Model):
    photo = models.ImageField(upload_to='media/client/images') 
    Web=models.URLField(max_length = 2000)
    
    @staticmethod
    def get_all_clntdata():
        return client.objects.all()
    
    def __str__(self):
        return self.photo.name
    
class contact(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    email = models.CharField(max_length=30)
    message = models.CharField(max_length=300)
    def __str__(self):
        return self.name
    
class subscribe(models.Model):
    email = models.CharField(max_length=30)

class portfolio(models.Model):
    name = models.CharField(max_length=20)
    sub_name = models.CharField(max_length=30)
    photo = models.ImageField(upload_to='media/portfolio/images')
    
    @staticmethod
    def get_all_portdata():
        return portfolio.objects.all()

    def __str__(self):
        return self.name
    
#  Start Sub_portfolio.........................................
    
class sub_portfolio(models.Model):
    name = models.CharField(max_length=20)
    sub_name = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='media/sub_portfolio/tech_portfolio/images')
    @staticmethod
    def get_all_subportdata():
        return sub_portfolio.objects.all()

    def __str__(self):
        return self.name
    
  
#  End Sub_portfolio.........................................


#   End   Index .........................................





# Start Reg Login Forgot................................................
 
# class registartion(models.Model):
#     email = models.CharField(max_length=30)
#     username=models.CharField(max_length=12)
#     password=models.CharField(max_length=12)
    # confirm_password=models.CharField(max_length=12)
    # birthdate=models.DateField(auto_now=False, auto_now_add=False)    
    # birth_date = models.DateField()
    # GENDER_CHOICES = (
    #     ('M', 'Male'),
    #     ('F', 'Female'),
    #     ('o', 'other'),
    # )
    # gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
        
    
    # PROFILE_CHOICES = (
    #     ('B', 'Businessman'),
    #     ('C', 'Client')
    # )
    # profile = models.CharField(max_length=1, choices=PROFILE_CHOICES)
    
    # phone_number = PhoneField(max_length=10,blank=True, help_text='Contact phone number')
    # phone_number = models.CharField(max_length=12)
    # phone_number = PhoneField(blank=True, help_text='Contact phone number')
    
    # @staticmethod
    # def get_all_ptdata(email):
    #     try:
    #         return registartion.object.get(email=email)
    #     except:
    #         return False
    
    # def __str__(self):
    #     return self.username
    
class reg(models.Model):
    email = models.CharField(max_length=30)
    username=models.CharField(max_length=12)
    password=models.CharField(max_length=12)
    birthdate = models.DateField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('o', 'other'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES) 
    
    PROFILE_CHOICES = (
        ('B', 'Businessman'),
        ('C', 'Client'),
    )
    profile = models.CharField(max_length=1, choices=PROFILE_CHOICES)
    phone_number = models.CharField(max_length=12)
    # phone_number = PhoneField(blank=True, help_text='Contact phone number')
    
    def __str__(self):
        return self.username
    
    @staticmethod
    def get_all_ptdata(email):
        try:
            return reg.object.get(email = email)
        except:
            return False
    
class login(models.Model):
    email = models.CharField(max_length=30)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    
    def __str__(self):
        return self.username
    
class forgot(models.Model):
    email = models.CharField(max_length=30)
    
 # End Reg Login Forgot................................................
 
 
 
 
    
    
# Satrt Category................................................
       
class category(models.Model):
    
    CAT_CHOICES = (
        ("Technology", "Technology"),
        ("Agriculture", "Agriculture"),
        ("Architecture","Architecture"),
        ("Book","Book"),
        ("Consultants","Consultants"),
        ("Catarers","Catarers"),
        ("Carpenters","Carpenters"),
        ("Electronics_applices","Electronics_applices"),
        ("Education","Education"),
        ("Fashion","Fashion"),
        ("Furnitures","Furnitures"),       
        ("Kids","Kids"),
        ("Pets","Pets"),
        ("Retail","Retail"),
        ("Real_estate","Real_estate"),
        ("Sell Cosmetic","Sell Cosmetic"),
        ("Vehical","Vehical"),
        )
  
    
    SUB_CHOICES = (
        ('Technology', (
            ('Sofware', 'Sofware'),
            ('Harware', 'Harware'),
            ('Web Development', 'Web Development'),
            ('Computer Repairing', 'Computer Repairing'),
            ('Digital Iteam Selling', 'Digital Iteam Selling'),
        )),
        
        ('Architecture', (
            ('Architectural Designer', 'Architectural Designer'),
            ('Urban Plan', 'Urban Plan'),
            ('Wooden Architecture','Wooden Architecture'),
        )),
        
        ('Agriculture', (
            ('Farming Business','Farming Business'),
            ('Equipment Resource','Equipment Resource'),
            ('Machinery Resource','Machinery Resource'),
            ('Products Storage','Products Storage'),
            ('Prodcut Seller','Prodcut Seller'),
        )),
        
        ('Book', (
            ('Special markets booksellers','Special markets booksellers'),
            ('Big box stores','Big box stores'),
            ('Price clubs','Price clubs'),
        )),
                
        ('Consultants', (
            ('Lowyer Advice','Lowyer Advice'),
            ('CA','CA'),
            ('Valuers','Valuers'),
        )),
        
        ('Catarers', (
            ('Birthday/Event/Function party','Birthday/Event/Function party'),
            ('Wedding Catarers','Wedding Catarers'),
        )),
        
        ('Carpenters', (
            ('Home Care','Home Care'),
            ('Wood Work','Wood Work'),
            ('Fabrication','Fabrication'),
        )),  
        
        ('Electronics_applices', (
            ('Computers & accessories','Computers & accessories'),
            ('Mobile','Mobile'),
            ('Tv - video - audio','Tv - video - audio'),
            ('Cameras & accessories','Cameras & accessories'),
            ('Games & Entertainment','Games & Entertainment'),
            ('Fridge - AC - Washing Machine','Fridge - AC - Washing Machine'),
            ('Kitchen','Kitchen'),
        )),
        
        ('Education', (
            ('Classes','Classes'),
            ('Coaching','Coaching'),
            ('Institute','Institute'),
        )), 
        
        ('Fashion', (
            ('Clothes','Clothes'),
            ('Footwear','Footwear'),
            ('Accessories','Accessories'),
        )), 
        
        ('Furnitures', (
            ('Sofa & Dining ','Sofa & Dining '),
            ('Beds & Wardrobes','Beds & Wardrobes'),
            ('Home Decor & Garden','Home Decor & Garden'),
            ('Other Household Items','Other Household Items'),
        )), 
        
        ('Kids', (
            ('Furniture And Toys','Furniture And Toys'),
            ('Prams & Walkers','Prams & Walkers'),
            ('Accessories','Accessories'),
        )),  
        
        ('Pets', (
            ('Dogs','Dogs'),
            ('Aquariums','Aquariums'),
            ('Pet Food & Accessories','Pet Food & Accessories'),
            ('Other Pets','Other Pets'),
        )), 
        
        ('Retail', (
            ('Grocery Store','Grocery Store'),
            ('Convenience Store','Convenience Store'),
            ('Hyper Market','Hyper Market'),
        )),
        
        ('Real_estate', (
            ('Residential','Residential'),
            ('Industrial','Industrial'),
            ('Commercial','Commercial'),
        )),
        
        ('Sell Cosmetic', (
            ('Beauty Parlours','Beauty Parlours'),
            ('Salon','Salon'),
            ('Spa','Spa'),
        )),
        
        ('Vehical', (
            ('Hiring','Hiring'),
            ('Commercial Vehicles','Commercial Vehicles'),
            ('Other Vehicles','Other Vehicles'),
            ('Spare Parts','Spare Parts'),
        )),
        
    )
    
    category = models.CharField(max_length = 50,choices = CAT_CHOICES,default = '1') 
    sub_category = models.CharField(max_length = 50,choices = SUB_CHOICES,default = '11')
    # sub_category = models.CharField(max_length = 20,choices = CAT_CHOICES,default = '1') 
    # sub_category = models.ForeignKey(sub,max_length=60,on_delete=models.CASCADE) 
    # sub_category = models.ForeignKey(sub,max_length = 20,choices = SUB_CHOICES,on_delete=models.CASCADE , default='11')
    # sub_cat = models.ForeignKey(sub,on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='media/category/images')
    
    @staticmethod
    def get_all_catdata():
        return category.objects.all()

    def __str__(self):
        return self.category
    

class cat_profile(models.Model):
    Desc = models.TextField(max_length=300)
    Price = models.DecimalField(max_digits= 5,decimal_places=2)
    photo = models.ImageField(upload_to='media/category/images')
    
    CITIES = (
        ('New York', 'New York'),
        ('Santa Monica', 'Santa Monica')
        # .. etc
    )
    city = models.CharField(max_length=55, choices=CITIES, blank=True)
    
    @staticmethod
    def get_all_capdata():
        return cat_profile.objects.all()

class sub(models.Model):
    sub_cat = models.CharField(max_length=50)
#   End Category..........................................
    
    
    
    
class Loan(models.Model):
    Bank_name=models.CharField(max_length=20)
    Loan_Type=models.CharField(max_length=30)
    Interest_Rate=models.CharField(max_length=50)
    Loan_Amount=models.CharField(max_length=20)
    Re_payment_Period=models.CharField(max_length=30)
    Address=models.URLField(max_length = 2000)
        
    @staticmethod
    def get_all_Loandata():
        return Loan.objects.all()
    
    def __str__(self):
        return self.Bank_name
        
class ClientRequest(models.Model):
    id = models.AutoField(primary_key=True)
    Client_email=models.CharField(max_length=50)
    Client_message=models.CharField(max_length=500)
    Client_Date=models.DateTimeField()
    Client_Mobile=models.CharField(max_length=15)
    Client_name=models.CharField(max_length=30)
    
    @staticmethod
    def get_all_cltreqdata():
        return ClientRequest.objects.all()
    
    def __str__(self):
        return self.Client_name


class Businessdetail(models.Model):
    
    
    MARKET_CHOICES = (
        ("GOOD", "GOOD"),
        ("AVERAGE", "AVERAGE"),
        ("PRO","PRO"),
        )
    
    BUSTYPE_CHOICES = (
        ("Technology", "Technology"),
        ("Agriculture", "Agriculture"),
        ("Architecture","Architecture"),
        ("Book","Book"),
        ("Consultants","Consultants"),
        ("Catarers","Catarers"),
        ("Carpenters","Carpenters"),
        ("Electronics_applices","Electronics_applices"),
        ("Education","Education"),
        ("Fashion","Fashion"),
        ("Furnitures","Furnitures"),       
        ("Kids","Kids"),
        ("Pets","Pets"),
        ("Retail","Retail"),
        ("Real_estate","Real_estate"),
        ("Sell Cosmetic","Sell Cosmetic"),
        ("Vehical","Vehical"),
        )
  
    
    Business_Shortdetail=models.CharField(max_length=500)
    Business_Detail=models.CharField(max_length=500)
    Business_Date=models.DateTimeField()
    Business_Brand=models.CharField(max_length=30)
    Business_Brandweb=models.URLField(max_length = 2000)
    Business_Mobile=models.CharField(max_length=15)
    Business_Email=models.CharField(max_length=50)
    Business_Type=models.CharField(max_length=30)
    Business_Turnover = models.CharField(max_length=15)
    Business_Type = models.CharField(max_length = 50,choices = BUSTYPE_CHOICES,default = '1')
    Business_Marketplace = models.CharField(max_length = 50,choices = MARKET_CHOICES,default = '1')
    Business_Features=models.CharField(max_length=800)
    
    @staticmethod
    def get_all_busdetdata():
        return Businessdetail.objects.all()
    
    def __str__(self):
        return self.Business_Type

class Businessslide(models.Model):
    slide = models.ImageField(upload_to='media/Businessslide/images') 
    
    @staticmethod
    def get_all_Bussliddata():
        return Businessslide.objects.all()


    

        
    