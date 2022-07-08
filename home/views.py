from email import message
from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView , CreateView , DeleteView
from django.urls import reverse_lazy
from admin_informations.models import AdminInformation
from django.contrib import messages
from django.http import HttpResponse

def home(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            # try:
            #     AdminInformation.objects.get(account_id=user.id)              
            #     return redirect('home:home')
            # except:
            #     AdminInformation.objects.create(account=user) 
            #     return redirect('home:home')
        else:
            messages.warning(request,"warning!")
    else:
        form = AuthenticationForm()
    return render(request,'index.html',{'form':form})


def SignUpView(request):
    if request.method == "POST":
            form = UserCreationForm(request.POST)

            if form.is_valid():
                user=form.save()
                login(request , user)
                return HttpResponse("User been created!")
        
    form = UserCreationForm()
    return render(request,'signup.html',{'form':form})

def LogOut(request):
	logout(request)
	return redirect('resturan:home')



def ListView(request):
	return render(request,'list_view.html',{})

def detailview(request):
	return render(request,'detail.html',{})


def savepost(request):
    return render(request,'save_post.html',{})