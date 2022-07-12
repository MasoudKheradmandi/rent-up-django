from django.http import HttpResponse
from django.shortcuts import render
from .forms import SaveFormAparteman
from .models import aparteman
# Create your views here.
def save_post(request):
    nevisande = request.user
    print(nevisande)
    if request.method == "POST":
        form = SaveFormAparteman(request.POST , request.FILES)
        if form.is_valid():
            titr = form.cleaned_data['titr']
            status_buy= form.cleaned_data['status_buy']
            gheymat= form.cleaned_data['gheymat']
            gheymat_rahn= form.cleaned_data['gheymat_rahn']
            gheymat_ejare= form.cleaned_data['gheymat_ejare']
            locations= form.cleaned_data['locations']
            sanad= form.cleaned_data['sanad']
            andaze= form.cleaned_data['andaze']
            tabaghe= form.cleaned_data['tabaghe']
            tedad_tabaghe= form.cleaned_data['tedad_tabaghe']
            tedad_vahed_tabaghe= form.cleaned_data['tedad_vahed_tabaghe']
            tedad_otagh= form.cleaned_data['tedad_otagh']
            tedad_dastshoe= form.cleaned_data['tedad_dastshoe']
            sal_sakht= form.cleaned_data['sal_sakht']
            ghabel_moaveze= form.cleaned_data['ghabel_moaveze']
            tozihat_karbar= form.cleaned_data['tozihat_karbar']
            tozihat_khososy= form.cleaned_data['tozihat_khososy']
            image= form.cleaned_data['image']
            active= form.cleaned_data['active']
            tahvie = form.cleaned_data['tahvie']
            internet = form.cleaned_data['internet']
            trass = form.cleaned_data['trass']
            wifi = form.cleaned_data['wifi']
            bed = form.cleaned_data['bed']
            micro = form.cleaned_data['micro']
            balcony = form.cleaned_data['balcony']
            sahel = form.cleaned_data['sahel']
            system_garmayeshi= form.cleaned_data['system_garmayeshi']
            sigary = form.cleaned_data['sigary']
            parking = form.cleaned_data['parking']
            x=aparteman.objects.create(
                titr=titr,status_buy=status_buy,gheymat=gheymat,gheymat_rahn=gheymat_rahn,gheymat_ejare=gheymat_ejare,locations=locations,sanad=sanad,andaze=andaze,tabaghe=tabaghe,
                tedad_tabaghe=tedad_tabaghe,tedad_vahed_tabaghe=tedad_vahed_tabaghe,tedad_otagh=tedad_otagh,
                tedad_dastshoe=tedad_dastshoe,sal_sakht=sal_sakht,ghabel_moaveze=ghabel_moaveze,tozihat_karbar=tozihat_karbar,
                tozihat_khososy=tozihat_khososy,image=image,active=active,
                internet=internet,trass=trass,wifi=wifi,bed=bed,micro=micro,balcony=balcony,sahel=sahel,system_garmayeshi=system_garmayeshi,sigary=sigary,parking=parking,tahvie=tahvie,nevisande=nevisande
            )
            x.save()
        return HttpResponse('Finish')
    else:
        form = SaveFormAparteman()
    
    context = {
        'form':form
    }
    return render(request,'save_post_apa.html',context)