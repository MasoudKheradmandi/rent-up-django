from django.shortcuts import render
from .forms import UserAccountForm
from admin_informations.models import AdminInformation
from django.contrib.auth.decorators import permission_required
# Create your views here.


@permission_required('is_staff',login_url='/')
def profile(request):
    account = request.user
    form = UserAccountForm()
    if request.method == "POST":
        form = UserAccountForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            Email = form.cleaned_data['Email']
            phone = form.cleaned_data['phone']
            phone_2=form.cleaned_data['phone_2']
            semat = form.cleaned_data['semat']
            address= form.cleaned_data['address']
            city = form.cleaned_data['city']
            code_posty = form.cleaned_data['code_posty']
            insta = form.cleaned_data['insta']
            whats_app =form.cleaned_data['whats_app']
            telegram=form.cleaned_data['telegram']
            about_me=form.cleaned_data['about_me']
            
            try:
                get_object = AdminInformation.objects.get(account=request.user)
                x = AdminInformation.objects.update(full_name=full_name,
                Email=Email,phone=phone,phone_2=phone_2,semat=semat,address=address,
                city=city,code_posty=code_posty,insta=insta,whats_app=whats_app,telegram=telegram,about_me=about_me
                )
            except:
                x = AdminInformation.objects.create(full_name=full_name,
                Email=Email,phone=phone,phone_2=phone_2,semat=semat,address=address,
                city=city,code_posty=code_posty,insta=insta,whats_app=whats_app,telegram=telegram,about_me=about_me,account=account
                )
            return render(request,'my-profile.html',{'form':form,'x':x,'get_object':AdminInformation.objects.get(account=request.user)})
        else:
            form = UserAccountForm()
    else:
        form = UserAccountForm()
        try:
            get_object = AdminInformation.objects.get(account=request.user)
            context = {
                'form':form,
                'get_object':get_object
            }
        except:
            context = {
                'form':form,               
            }

    return render(request,'my-profile.html',context)