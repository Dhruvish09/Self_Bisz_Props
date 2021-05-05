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
    Web=models.URLField(max_length = 2000)
    
    @staticmethod
    def get_all_clntdata():
        return client.objects.all()
    
    def __str__(self):
        return self.photo.name


class portfolio(models.Model):
    name = models.CharField(max_length=20)
    sub_name = models.CharField(max_length=30)
    photo = models.ImageField(upload_to='media/portfolio/images')
    
    @staticmethod
    def get_all_portdata():
        return portfolio.objects.all()

    def __str__(self):
        return self.name
    
class sub_portfolio(models.Model):
    name = models.CharField(max_length=20)
    sub_name = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='media/sub_portfolio/tech_portfolio/images')
    @staticmethod
    def get_all_subportdata():
        return sub_portfolio.objects.all()

    def __str__(self):
        return self.name
    

            
class Contactus(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=250,null=True, blank=True)
    mobile = models.CharField(max_length=12,null=True, blank=True)
    subject = models.CharField(max_length=300)
    message = models.TextField()
    added_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Contact Us"
    

class subscribe(models.Model):
    email = models.CharField(max_length=30)
    
    def __str__(self):
        return   'email id'+ ':' + self.email

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

#   End  Index Area .........................................


#   Start Reg Area................................................
     
class reg(models.Model):
    photo = models.ImageField(upload_to='media/profilephoto/images')
    email = models.CharField(max_length=30)
    username=models.CharField(max_length=12)
    password=models.CharField(max_length=264)
    c_password=models.CharField(max_length=264)
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
    empAuth_objects = models.Manager()
        
    
#   End Reg Area ................................................


    
# Start Business Area.............................................   
           
class Businessdetail(models.Model):
    
    
    MARKET_CHOICES = (
        ("Monopolic", "Monopolic"),
        ("Non-Monopolic", "Non-Monopolic"),
        )

    # CITY_CHOICES = (
    #     ("Ahmedabad", "Ahmedabad"),
    #     ("Surat", "Surat"),
    #     )

    # COUNTRY_CHOICES = (
    #     ("IND", "IND"),
    #     ("USA", "USA"),
    #     )

    # BUSMARKET_CHOICES = (
    #     ("Monopolistic", "Monopolistic"),
    #     ("Non-Monopolistic", "Non-Monopolistic"),
    #     )
    
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
    Business_Turnover = models.CharField(max_length=15)
    # Business_Market_Type = models.CharField(max_length = 50,choices = BUSMARKET_CHOICES,default = '1')
    # Business_City = models.CharField(max_length = 60,choices = CITY_CHOICES,default = '1')
    # Business_Country = models.CharField(max_length = 60,choices = COUNTRY_CHOICES,default = '1')
    # Business_Address=models.TextField(max_length=500)
    Business_Type = models.CharField(max_length = 50,choices = BUSTYPE_CHOICES,default = '1')
    Business_Marketplace = models.CharField(max_length = 50,choices = MARKET_CHOICES,default = '1')
    Business_Features=models.CharField(max_length=800)

  
    @staticmethod
    def get_all_busdetdata():
        return Businessdetail.objects.all()
    
    def __str__(self):
        return 'Type of Business is:-'+ self.Business_Type



class Businessslide(models.Model):
    slide = models.ImageField(upload_to='media/Businessslide/images') 
    
    @staticmethod
    def get_all_Bussliddata():
        return Businessslide.objects.all()

    def __str__(self):
        return 'Uploaded Image is:'+ self.slide.name

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
        return 'You Have Request From' + ':' + self.Client_name

# End Business Area...............................................    

        
    