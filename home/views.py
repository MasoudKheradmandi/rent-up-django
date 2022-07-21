from django.shortcuts import render, redirect ,get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.http import HttpResponse 
from posts.models import aparteman , vilae
from .models import CommentAparteman,CommentVilla
from .forms import CommentFormAparteman,CommentFormVillae



def home(request):
    # if "register" in request.method == "POST":

    #     return render(request,'index.html',{'form':form})
    if request.method == "POST":
        if request.POST.get('submit') == 'sign_in':
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
            else:
                messages.warning(request, "warning!")
        elif request.POST.get('submit') == 'register':
            print('vorod')
            form = UserCreationForm(request.POST)
            if form.is_valid():
                print("formisvalid")
                user = form.save()
                login(request, user)
                return HttpResponse("User been created!")
            else:
                messages.warning(request, "warning!")
    else:
        form = UserCreationForm()
    return render(request, 'index.html', {})


def LogOut(request):
    logout(request)
    return redirect('resturan:home')


def list_view_aparteman(request):
    posts = aparteman.objects.all()
    context = {
        "posts": posts,
        "count": posts.count()
    }
    return render(request, 'list_view_apa.html', context)




def list_view_vila(request):
    posts = vilae.objects.all()
    context = {
        "posts": posts,
        "count": posts.count()
    }
    return render(request, 'list_view_vila.html', context)



def detail_view_vila(request,id):
    post = get_object_or_404(vilae,id=id)
    comments = CommentVilla.objects.filter(is_active=True,Villae_id=id)
    new_comment = None
    if request.method == "POST":
        comment_form = CommentFormVillae(request.POST)
        if comment_form.is_valid():
            Full_name = comment_form.cleaned_data['Full_name']
            Email_address = comment_form.cleaned_data['Email_address']
            message = comment_form.cleaned_data['message']
            new_comment = CommentVilla.objects.create(
                Full_name=Full_name,Email_address=Email_address,message=message,Villae=post,
                )
            new_comment.save()
    else:
        comment_form = CommentFormVillae()
    context={
        
        'post' : post,
        'comments':comments,
        "comment_form":comment_form,
    }
    return render(request, 'detail_vila.html', context)



def detail_view_apa(request,id):

    post = get_object_or_404(aparteman,id=id)

    comments = CommentAparteman.objects.filter(is_active=True,Aparteman_id=id)
    new_comment = None
    if request.method == "POST":
        comment_form = CommentFormAparteman(request.POST)
        if comment_form.is_valid():
            Full_name = comment_form.cleaned_data['Full_name']
            Email_address = comment_form.cleaned_data['Email_address']
            message = comment_form.cleaned_data['message']
            new_comment = CommentAparteman.objects.create(
                Full_name=Full_name,Email_address=Email_address,message=message,Aparteman=post,
                )
            new_comment.save()
    else:
        comment_form = CommentFormAparteman()
    context={
        'post' : post,
        'comments':comments,
        "comment_form":comment_form,
    }
    return render(request, 'detail_apa.html', context)




def savepost(request):
    return render(request, 'save_post.html', {})
