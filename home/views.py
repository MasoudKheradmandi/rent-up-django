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
    # if "register" in request.method == "POST":

    #     return render(request,'index.html',{'form':form})
    if  request.method == "POST":
        if request.POST.get('submit') == 'sign_in':
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request,user)
            else:
                messages.warning(request,"warning!")
        elif request.POST.get('submit') == 'register' :
            print('vorod')
            form = UserCreationForm(request.POST)
            if form.is_valid():
                print("formisvalid")
                user=form.save()
                login(request , user)
                return HttpResponse("User been created!")
            else:
                messages.warning(request,"warning!")
    else :
        form = UserCreationForm()
    return render(request,'index.html',{})




def LogOut(request):
	logout(request)
	return redirect('resturan:home')



def ListView(request):
	return render(request,'list_view.html',{})

def detailview(request):
	return render(request,'detail.html',{})


def savepost(request):
    return render(request,'save_post.html',{})