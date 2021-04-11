from django.db import models
from phone_field import PhoneField
from django import forms

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
    
class tech_portfolio(models.Model):
    name = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='media/sub_portfolio/tech_portfolio/images')
    
    @staticmethod
    def get_all_techportdata():
        return tech_portfolio.objects.all()

    def __str__(self):
        return self.name
    
class auto_portfolio(models.Model):
    name = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='media/sub_portfolio/auto_portfolio/images')
    
    @staticmethod
    def get_all_autoportdata():
        return auto_portfolio.objects.all()

    def __str__(self):
        return self.name

class book_portfolio(models.Model):
    name = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='media/sub_portfolio/book_portfolio/images')
    
    @staticmethod
    def get_all_bookportdata():
        return book_portfolio.objects.all()

    def __str__(self):
        return self.name
    
class retail_portfolio(models.Model):
    name = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='media/sub_portfolio/retail_portfolio/images')
    
    @staticmethod
    def get_all_retailportdata():
        return retail_portfolio.objects.all()

    def __str__(self):
        return self.name
    
class real_portfolio(models.Model):
    name = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='media/sub_portfolio/real_portfolio/real_portfolio/images')
    
    @staticmethod
    def get_all_realportdata():
        return real_portfolio.objects.all()

    def __str__(self):
        return self.name
   
class furniture_portfolio(models.Model):
    name = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='media/sub_portfolio/real_portfolio/furniture_portfolio/images')
    
    @staticmethod
    def get_all_furniportdata():
        return furniture_portfolio.objects.all()

    def __str__(self):
        return self.name
  
#  End Sub_portfolio.........................................


#   End   Index .........................................





# Start Reg Login Forgot................................................
 
class registartion(models.Model):
    email = models.CharField(max_length=30)
    username=models.CharField(max_length=12)
    password=models.CharField(max_length=12)
    confirm_password=models.CharField(max_length=12)
    bday=models.DateField(auto_now=False, auto_now_add=False)    
    # birth_date = models.DateField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('o', 'other'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
        
    
    PROFILE_CHOICES = (
        ('B', 'Businessman'),
        ('C', 'Client')
    )
    profile = models.CharField(max_length=1, choices=PROFILE_CHOICES)
    
    phone_number = PhoneField(max_length=10,blank=True, help_text='Contact phone number')
    # phone_number = models.CharField(max_length=12)
    # phone_number = PhoneField(blank=True, help_text='Contact phone number')
    
    def __str__(self):
        return self.username
    
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
            ('11', 'Sofware'),
            ('12', 'Harware'),
            ('13', 'Web Development'),
            ('13', 'Computer Repairing'),
            ('13', 'Digital Iteam Selling'),
        )),
        
        ('Architecture', (
            ('21', 'Architectural Designer'),
            ('22', 'Urban Plan'),
            ('23', 'Wooden Architecture'),
        )),
        
        ('Agriculture', (
            ('31', 'Farming Business'),
            ('32', 'Equipment Resource'),
            ('33', 'Machinery Resource'),
            ('34', 'Products Storage'),
            ('35', 'Prodcut Seller'),
        )),
        
        ('Book', (
            ('41', 'Special markets booksellers'),
            ('42', 'Big box stores'),
            ('43', 'Price clubs'),
        )),
                
        ('Consultants', (
            ('51', 'Lowyer Advice'),
            ('52', 'CA'),
            ('53', 'Valuers'),
        )),
        
        ('Catarers', (
            ('61', 'Birthday/Event/Function party'),
            ('62', 'Wedding Catarers'),
        )),
        
        ('Carpenters', (
            ('71', 'Home Care'),
            ('72', 'Wood Work'),
            ('73', 'Fabrication'),
        )),  
        
        ('Electronics_applices', (
            ('81', 'Computers & accessories'),
            ('82', 'Mobile'),
            ('83', 'Tv - video - audio'),
            ('84', 'Cameras & accessories'),
            ('85', 'Games & Entertainment'),
            ('86', 'Fridge - AC - Washing Machine'),
            ('87', 'Kitchen'),
        )),
        
        ('Education', (
            ('91', 'Classes'),
            ('92', 'Coaching'),
            ('93', 'Institute'),
        )), 
        
        ('Fashion', (
            ('101', 'Clothes'),
            ('102', 'Footwear'),
            ('103', 'Accessories '),
        )), 
        
        ('Furnitures', (
            ('111', 'Sofa & Dining '),
            ('112', 'Beds & Wardrobes '),
            ('113', 'Home Decor & Garden'),
            ('114', 'Other Household Items'),
        )), 
        
        ('Kids', (
            ('121', 'Furniture And Toys'),
            ('122', 'Prams & Walkers'),
            ('123', 'Accessories'),
        )),  
        
        ('Pets', (
            ('131', 'Dogs'),
            ('132', 'Aquariums'),
            ('133', 'Pet Food & Accessories'),
            ('134', 'Other Pets'),
        )), 
        
        ('Retail', (
            ('141', 'Grocery Store'),
            ('142', 'Convenience Store'),
            ('143', 'Hyper Market'),
        )),
        
        ('Real_estate', (
            ('151', 'Residential'),
            ('152', ' Industrial'),
            ('153', ' Commercial'),
        )),
        
        ('Sell Cosmetic', (
            ('161', 'Beauty Parlours'),
            ('162', 'Salon'),
            ('163', 'Spa'),
        )),
        
        ('Vehical', (
            ('171', 'Hiring'),
            ('172', 'Commercial Vehicles'),
            ('173', 'Other Vehicles'),
            ('174', 'Spare Parts'),
        )),
        
    )
    
    category = models.CharField(max_length = 20,choices = CAT_CHOICES,default = '1') 
    sub_category = models.CharField(max_length = 20,choices = SUB_CHOICES,default = '11')
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
    


