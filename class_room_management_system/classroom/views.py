from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from . models import *
from datetime import datetime
# Create your views here.

@login_required(login_url='login')
def primary(request):
    return HttpResponse("<h1>Sust Class Room Management System</h1>")


def loginPage(request):

    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method=="POST":

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username,password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or Password is incorrect')
            
        context = {'name':"Mozammal Hossain"}
        return render(request,'login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('primary')
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account has created for "+ form.cleaned_data.get('username'))
            return redirect('login')
    context={'form':form}
    return render(request, 'signup.html', context)

def mainView(request):
    return render(request, 'main.html')

def homeView(request):
    return render(request,'home.html')

def academicbuildings(request):
    buildinglist = Building.objects.all()
    context = {'buildinglist':buildinglist}
    return render(request,'buildings.html',context)

def calender_page(request):
    if request.method=="POST":
        date = request.POST.get('date')
        date = datetime.strptime(date,'%m/%d/%Y')
        date = date.strftime('%Y-%m-%d')
        print(date)
    return render(request,'calender.html')

def classrooms_views(request,name,id):
    classroomlist = Classroom.objects.filter(building__name__contains=name)
    return render(request,'classrooms.html',{'id':classroomlist,'building_name':id})

def classroomdetailview(request,id,name):
    result = 0
    classroom_details = Classroom.objects.get(room_no=id,building=name)
    
    if request.method=="POST":
        date = request.POST.get('date')
        date = datetime.strptime(date,'%m/%d/%Y')
        date = date.strftime('%Y-%m-%d')
        print(date)
        user = request.user
        # schedule, created = ClassTime.objects.get_or_create(date=date,classroom=classroom_details)
        result = Track.objects.filter(date=date,classroom=classroom_details)
        schedule=[]
        for r in result:
            schedule.append(r.time)
        print(schedule)
        print("Mozammal Hossain")
        # print(created)
        return render(request,'classschedule.html',{'schedule':schedule})
        


    classroom_details = Classroom.objects.get(room_no=id,building=name)
    return render(request,'classroomdetail.html',{'details':classroom_details})

def my_schedule(request):
    user = request.user
    schedule = Track.objects.filter(user=user)
    print(schedule)
    return render(request,'myschedule.html',{'schedule':schedule})