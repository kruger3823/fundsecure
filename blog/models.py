from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Register(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    address=models.CharField(max_length=50)

    def __str__(self):
        return str(self.user.username)


class FileUpload(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=50)
    file=models.FileField(upload_to='files')
    date=models.DateTimeField(default=timezone.now)


class InssuranceType(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return str(self.name)



class InsuranceApply(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    profilepic=models.ImageField(upload_to='images')
    age=models.IntegerField()
    date_of_birth=models.DateField()
    male='male'
    female='female'
    genders=[(male,'male'),(female,'female')]
    gender=models.CharField(max_length=20,choices=genders,default=male)
    state=models.CharField(max_length=15)
    country=models.CharField(max_length=15)
    district=models.CharField(max_length=15)
    city=models.CharField(max_length=25)
    income=models.IntegerField()
    phone=PhoneNumberField()
    insurance_type=models.ForeignKey(InssuranceType,on_delete=models.CASCADE)
    nominee_name=models.CharField(max_length=30)
    nominee_address=models.TextField()
    date=models.TextField()
    def __str__(self):
        return str(self.user.username)

class Complaint(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    age=models.IntegerField()
    date_of_birth=models.DateField()
    male='male'
    female='female'
    genders=[(male,'male'),(female,'female')]
    gender=models.CharField(max_length=20,choices=genders,default=male)
    state=models.CharField(max_length=15)
    country=models.CharField(max_length=15)
    district=models.CharField(max_length=15)
    city=models.CharField(max_length=25)
    income=models.IntegerField()
    phone=PhoneNumberField()
    insurance_type=models.ForeignKey(InssuranceType,on_delete=models.CASCADE)
    nominee_name=models.CharField(max_length=30)
    nominee_address=models.TextField()
    date=models.TextField()
    complaint=models.TextField()
    def __str__(self):
         return str(self.user.username)




class Post(models.Model):
    income= models.IntegerField()
    experience= models.CharField(max_length=300)
    strength=models.CharField(max_length=300)
    senior=models.CharField(max_length=300)
    childrencount=models.IntegerField()
    agegroup=models.CharField(max_length=300)
    disabilities=models.CharField(max_length=300)
    employers=models.CharField(max_length=300)
    casualities=models.CharField(max_length=300)
    increments=models.CharField(max_length=300)
    lifestyle=models.CharField(max_length=300)














class Worker(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    profile_pic= models.ImageField(upload_to='profile_pic/CustomerProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_instance(self):
        return self
    def __str__(self):
        return self.user.first_name


class insurance_scheme(models.Model):
    policyno = models.CharField(max_length=200, null=True)
    insurancetype = models.CharField(max_length=200, null=True)
    company = models.CharField(max_length=200, null=True)
    policyDescription = models.CharField(max_length=200, null=True)
    timelength = models.CharField(max_length=200, null=True)
    insuranceamount = models.CharField(max_length=200, null=True)


class Apply(models.Model):
    name = models.CharField(max_length=200, null=True)
    policyno = models.CharField(max_length=200, null=True)
    insurancetype = models.CharField(max_length=200, null=True)
    company = models.CharField(max_length=200, null=True)
    policyDescription = models.CharField(max_length=200, null=True)
    timelength = models.CharField(max_length=200, null=True)
    insuranceamount = models.CharField(max_length=200, null=True)