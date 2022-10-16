from os import name
from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponseRedirect,HttpResponse
from .forms import *
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import logout,login,authenticate
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Post
from django.contrib.auth.models import Group
# Create your views here.
def index(request):
    return render(request,'index.html',)

def results(request):
    return render(request,'results.html',)
def register(request):
    registered=False
    if request.method=="POST":
        user_form=UserForm(data=request.POST)
        profile_form=ProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.save()

            profile=profile_form.save(commit=False)
            profile.user=user
            profile.save()
            registered=True

        else:
            HttpResponse('invalid form')
    
    else:
        user_form=UserForm()
        profile_form=ProfileForm()

    return render(request,'register.html',{'registered':registered,'user_form':user_form,'profile_form':profile_form})

def user_login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('dashboard'))
            else:
                return HttpResponse('user deactivated')
        else:
            return HttpResponse('invalid user name or password')
    else:
        return render(request,'login.html')

def dashboard(request):
    return render(request,'dashboard.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('index')

def change_password(request):
    if request.method=="POST":
        form=PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user=form.save()
            update_session_auth_hash(request,user)
            messages.success(request,"Password Updated")
            return render(request,"change_password.html")
        else:
            messages.error(request,"Correct Your Error!")
    else:
        form=PasswordChangeForm(request.user)
    return render(request,"change_password.html",{'form':form})



def fileupload(request):

    if request.method=="POST":
        fileupload_form=FileUploadForm(request.POST,request.FILES)
        if fileupload_form.is_valid():
            cp=FileUpload(user=request.user,name=fileupload_form.cleaned_data['name'],file=fileupload_form.cleaned_data['file'])
            cp.save()

            return redirect('myfiles')
        else:
            return HttpResponse("invalid form")
    fileupload_form=FileUploadForm()
    return render(request,'fileupload.html',{'form':fileupload_form})
def myfiles(request):

    files=FileUpload.objects.all().order_by('-date')
    return render(request,'myfiles.html',{'files':files})

def createpost(request):
        if request.method == 'POST':
            if request.POST.get('income') and request.POST.get('experience') and request.POST.get('senior') and request.POST.get('experience') and request.POST.get('agegroup'):
                post=Post()
                post.title= request.POST.get('income')
                post.content= request.POST.get('experience')
                post.strength=request.POST.get('strength')
                post.senior=request.POST.get('senior')
                post.agegroup=request.POST.get('agegroup')
                post.childrencount=request.POST.get('childrencount')
                post.disabilities=request.POST.get('disabilities')
                post.employers=request.POST.get('employers')
                post.casualities=request.POST.get('casualities')
                post.increments=request.POST.get('increments')
                post.lifestyle=request.POST.get('lifestyle')
                riskfactor=""
                print(post.title)
                print(post.content)
                opinion=""
                safety=0
                income=int(post.title)
                income=income/100000
                income=int(income)
                if(income>5):
                    safety=safety+1
                else:
                    riskfactor=riskfactor+ "  Annual Income Seems Too Low ,"
                experience=post.content
                experience=int(experience)
                print(experience)
                if(experience>5):
                    safety=safety+1
                strength=post.strength
                print(strength)
                strength=int(strength)
                if(strength<3):
                    safety=safety+1
                senior=post.senior
                senior=int(senior)
                if(senior<3):
                    safety=safety+1
                else:
                    safety=safety-1
                    riskfactor=riskfactor+ " Too Many Senior Members And Chances For Death ,"
                agegroup=post.agegroup
                agegroup=int(agegroup)
                if(agegroup>50):
                    safety=safety-1
                    riskfactor=riskfactor+ " Family Members Age Aggregate Is Near To Senior Level ,"
                childrencount=post.childrencount
                childrencount=int(childrencount)
                if(childrencount>3):
                    safety=safety-1
                disabilities=post.disabilities
                #disabilities=int(disabilities)
                if(disabilities=="Yes"):
                    safety=safety-1
                    riskfactor=riskfactor+ " Risk of Disabled persons in the Scheme ,"
                else:
                    safety=safety+1
                employers=post.employers
                employers=int(employers)
                if(employers>6):
                    safety=safety+2
                else:
                    safety=safety+1
                casualities=post.casualities
                casualities=int(casualities)
                if(casualities>5):
                    safety=safety-3
                    riskfactor=riskfactor+ "Too many casualities In The Near By Past, "
                increments=post.increments
                increments=int(increments)
                if(increments>3):
                    safety=safety+1
                else:
                    safety=safety-1
                lifestyle=post.lifestyle
                if(lifestyle=="yes"):
                    safety=safety-2
                    riskfactor=riskfactor+ "Being Alcoholic Is A Huge Risk"
                else:
                    safety=safety+1
                print('safety')
                print(safety)
                percentage=(safety/11)*100
                print('percentage')
                print(percentage)
                print(percentage)
                risklevel=""
                if(percentage>20 and percentage<100):
                    risklevel="Low Risk"
                elif(percentage<50 and percentage>20):
                    risklevel="Medium Risk"
                elif(percentage>=0 and percentage<20):
                    risklevel="High Risk"
                print("Risk Level")
                print(risklevel)
                print("Risk Factor")
                print(riskfactor)
                if(risklevel=="Low Risk"):
                    opinion="Can Be Processed"
                elif(risklevel=="Medium Risk"):
                    opinion="Proceed With Extreme Care"
                elif(risklevel=="High Risk"):
                    opinion="Advice To Reject The Form"
                #post.save()
                
                return render(request, 'results.html',context={'Risk_percentage':safety,'Risk_level':risklevel,'Risk_factors':riskfactor,'Risk_opinion':opinion})  

        else:
                return render(request,'dashboard.html')






















def registerUserpage(request):
    userForm= WorkerUserForm()
    workerForm= WorkerForm()
    mydict={'userForm':userForm,'workerForm':workerForm}
    if request.method=='POST':
        userForm= WorkerUserForm(request.POST)
        customerForm= WorkerForm(request.POST, request.FILES)
        if userForm.is_valid() and customerForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            print(user)
            worker=customerForm.save(commit=True)
            worker.user=user
            worker.save()
            print(worker)
            my_worker_group = Group.objects.get_or_create(name='CUSTOMER')
            my_worker_group[0].user_set.add(user)
        return redirect('/doctorlogin')
    return render(request,'workersignup.html',context=mydict)


def is_cus(user):
    return user.groups.filter(name='CUSTOMER').exists()


def afterlogin_view(request):
    if is_cus(request.user):
        return redirect('dashboard1')



def dashboard1(request):
    insurance_view = insurance_scheme.objects.all()
    return render(request, 'dashboard1.html', {'insurance_view': insurance_view})





def add_scheme(request):
    if request.method == "POST":
        policyno = request.POST.get('policyno')
        insurancetype= request.POST.get('insurancetype')
        company = request.POST.get('company')
        timelength = request.POST.get('timelength')
        policyDescription = request.POST.get('policyDescription')
        insuranceamount = request.POST.get('insuranceamount')

        insurance_scheme(policyno=policyno,insurancetype=insurancetype,company=company,timelength=timelength,policyDescription=policyDescription,insuranceamount=insuranceamount).save()
    return render(request,'add_scheme.html')


def apply(request):

    if request.method == "POST":
        name = request.POST.get('policyno')
        policyno = request.POST.get('policyno')
        insurancetype = request.POST.get('insurancetype')
        company = request.POST.get('company')
        timelength = request.POST.get('timelength')
        policyDescription = request.POST.get('policyDescription')
        insuranceamount = request.POST.get('insuranceamount')

        Apply(name=name,policyno=policyno, insurancetype=insurancetype, company=company, timelength=timelength,
                         policyDescription=policyDescription, insuranceamount=insuranceamount).save()
    return render(request,'apply_scheme.html')


def view_scheme(request):
    insurance_view = Apply.objects.all()
    return render(request, 'view_scheme.html', {'insurance_view': insurance_view})