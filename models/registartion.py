from django.db import models
# from phone_field import PhoneField

# Create your models here.
# class registartion(models.Model):
#     email = models.CharField(max_length=30)
#     username=models.CharField(max_length=12)
#     password=models.CharField(max_length=12)
#     confirm_password=models.CharField(max_length=12)
#     birth_date = models.DateField()
#     GENDER_CHOICES = (
#         ('M', 'Male'),
#         ('F', 'Female'),
#         ('o', 'other'),
#     )
#     gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
#     phone_number = models.CharField(max_length=12)
#     # phone_number = PhoneField(blank=True, help_text='Contact phone number')
    
#     def __str__(self):
#         return self.username
    

class registartion(models.Model):
    email = models.CharField(max_length=30)
    username=models.CharField(max_length=12)
    password=models.CharField(max_length=12)
    confirm_password=models.CharField(max_length=12)
    birth_date = models.DateField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('o', 'other'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone_number = PhoneField(blank=True, help_text='Contact phone number')
    # phone_number = models.CharField(max_length=12)
    # phone_number = PhoneField(blank=True, help_text='Contact phone number')
    
    def __str__(self):
        return self.username


