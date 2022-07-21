from django.http import HttpResponse
from django.shortcuts import render
from .forms import SaveFormAparteman, SavePostvillae, SavePostZamin
from .models import aparteman, vilae, vilae_image, zamin, aparteman_images, zamin_image

def save_post(request):
    return render(request,'save_post.html')

def save_post_apa(request):
    nevisande = request.user
    if request.method == "POST":
        form = SaveFormAparteman(request.POST, request.FILES)
        # form_images = SavePostApa(request.FILES)
        if form.is_valid():
            titr = form.cleaned_data['titr']
            status_buy = form.cleaned_data['status_buy']
            gheymat = form.cleaned_data['gheymat']
            gheymat_rahn = form.cleaned_data['gheymat_rahn']
            gheymat_ejare = form.cleaned_data['gheymat_ejare']
            locations = form.cleaned_data['locations']
            sanad = form.cleaned_data['sanad']
            andaze = form.cleaned_data['andaze']
            tabaghe = form.cleaned_data['tabaghe']
            tedad_tabaghe = form.cleaned_data['tedad_tabaghe']
            tedad_vahed_tabaghe = form.cleaned_data['tedad_vahed_tabaghe']
            tedad_otagh = form.cleaned_data['tedad_otagh']
            tedad_dastshoe = form.cleaned_data['tedad_dastshoe']
            sal_sakht = form.cleaned_data['sal_sakht']
            ghabel_moaveze = form.cleaned_data['ghabel_moaveze']
            tozihat_karbar = form.cleaned_data['tozihat_karbar']
            tozihat_khososy = form.cleaned_data['tozihat_khososy']
            image = form.cleaned_data['image']
            active = form.cleaned_data['active']
            tahvie = form.cleaned_data['tahvie']
            internet = form.cleaned_data['internet']
            trass = form.cleaned_data['trass']
            wifi = form.cleaned_data['wifi']
            bed = form.cleaned_data['bed']
            micro = form.cleaned_data['micro']
            balcony = form.cleaned_data['balcony']
            sahel = form.cleaned_data['sahel']
            system_garmayeshi = form.cleaned_data['system_garmayeshi']
            sigary = form.cleaned_data['sigary']
            parking = form.cleaned_data['parking']
            # this is Big Bug !!!!!!
            images = request.FILES.getlist('images')
            x = aparteman.objects.create(
                titr=titr, status_buy=status_buy, gheymat=gheymat, gheymat_rahn=gheymat_rahn, gheymat_ejare=gheymat_ejare, locations=locations, sanad=sanad, andaze=andaze, tabaghe=tabaghe,
                tedad_tabaghe=tedad_tabaghe, tedad_vahed_tabaghe=tedad_vahed_tabaghe, tedad_otagh=tedad_otagh,
                tedad_dastshoe=tedad_dastshoe, sal_sakht=sal_sakht, ghabel_moaveze=ghabel_moaveze, tozihat_karbar=tozihat_karbar,
                tozihat_khososy=tozihat_khososy, image=image, active=active,
                internet=internet, trass=trass, wifi=wifi, bed=bed, micro=micro, balcony=balcony, sahel=sahel, system_garmayeshi=system_garmayeshi, sigary=sigary, parking=parking, tahvie=tahvie, nevisande=nevisande,
            )
            x.save()
            for ima in images:
                y = aparteman_images.objects.create(images=ima, place=x)
                y.save()
            return HttpResponse('Finish')
    else:
        form = SaveFormAparteman()

    context = {
        'form': form,
        "sabt": "aparteman"
    }
    return render(request, 'save_post.html', context)


def save_post_villa(request):
    nevisande = request.user
    if request.method == "POST":
        form = SavePostvillae(request.POST, request.FILES)
        if form.is_valid():
            titr = form.cleaned_data['titr']
            status_buy = form.cleaned_data['status_buy']
            gheymat = form.cleaned_data['gheymat']
            gheymat_rahn = form.cleaned_data['gheymat_rahn']
            gheymat_ejare = form.cleaned_data['gheymat_ejare']
            locations = form.cleaned_data['locations']
            sanad = form.cleaned_data['sanad']
            andaze_zamin = form.cleaned_data['andaze_zamin']
            andaze_bana = form.cleaned_data['andaze_bana']
            tedad_otagh = form.cleaned_data['tedad_otagh']
            tedad_dastshoe = form.cleaned_data['tedad_dastshoe']
            sal_sakht = form.cleaned_data['sal_sakht']
            ghabel_moaveze = form.cleaned_data['ghabel_moaveze']
            tozihat_karbar = form.cleaned_data['tozihat_karbar']
            tozihat_khososy = form.cleaned_data['tozihat_khososy']
            image = form.cleaned_data['image']
            active = form.cleaned_data['active']
            tahvie = form.cleaned_data['tahvie']
            internet = form.cleaned_data['internet']
            trass = form.cleaned_data['trass']
            wifi = form.cleaned_data['wifi']
            bed = form.cleaned_data['bed']
            micro = form.cleaned_data['micro']
            balcony = form.cleaned_data['balcony']
            sahel = form.cleaned_data['sahel']
            system_garmayeshi = form.cleaned_data['system_garmayeshi']
            sigary = form.cleaned_data['sigary']
            parking = form.cleaned_data['parking']
            images = request.FILES.getlist('images')
            x = vilae.objects.create(
                titr=titr, status_buy=status_buy, gheymat=gheymat, gheymat_rahn=gheymat_rahn, gheymat_ejare=gheymat_ejare, locations=locations, sanad=sanad, andaze_zamin=andaze_zamin, tedad_otagh=tedad_otagh,
                tedad_dastshoe=tedad_dastshoe, sal_sakht=sal_sakht, ghabel_moaveze=ghabel_moaveze, tozihat_karbar=tozihat_karbar,
                tozihat_khososy=tozihat_khososy, image=image, active=active,
                internet=internet, trass=trass, wifi=wifi, bed=bed, micro=micro, balcony=balcony, sahel=sahel, system_garmayeshi=system_garmayeshi, sigary=sigary, parking=parking, tahvie=tahvie, nevisande=nevisande, andaze_bana=andaze_bana
            )
            x.save()
            for ima in images:
                y = vilae_image.objects.create(images=ima, place=x)
                y.save()
            return HttpResponse('Finish')
    else:
        form = SavePostvillae()

    context = {
        'form': form,
        'sabt': "villa"

    }
    return render(request, 'save_post.html', context)


def save_post_zamin(request):
    nevisande = request.user
    if request.method == "POST":
        form = SavePostZamin(request.POST, request.FILES)
        if form.is_valid():
            titr = form.cleaned_data['titr']
            gheymat = form.cleaned_data['gheymat']
            andaze = form.cleaned_data['andaze']
            noe_zamin = form.cleaned_data['noe_zamin']
            locations = form.cleaned_data['locations']
            sanad = form.cleaned_data['sanad']
            ghabel_moaveze = form.cleaned_data['ghabel_moaveze']
            tozihat_karbar = form.cleaned_data['tozihat_karbar']
            tozihat_khososy = form.cleaned_data['tozihat_khososy']
            image = form.cleaned_data['image']
            active = form.cleaned_data['active']
            images = request.FILES.getlist('images')
            x = zamin.objects.create(
                titr=titr, gheymat=gheymat, noe_zamin=noe_zamin, locations=locations,
                sanad=sanad, ghabel_moaveze=ghabel_moaveze, tozihat_karbar=tozihat_karbar,
                tozihat_khososy=tozihat_khososy,
                image=image, active=active, nevisande=nevisande, andaze=andaze
            )
            x.save()
            for ima in images:
                y = zamin_image.objects.create(images=ima, place=x)
                y.save()
            return HttpResponse("Done!")
    else:
        form = SavePostZamin()

    context = {
        'form': form
    }
    return render(request, 'save_post_zamin.html', context)

def compare_post_f(request,noe,id):
    if noe == 'aparteman':
        post = aparteman.objects.get(id=id)
    elif noe == 'vilae':
        post = vilae.objects.get(id=id)
    context={
        'post' : post,
        'noe' :noe,
    }
    return render(request,'compare-property.html',context)

def choose_to_compare(request,noe):
    f_id=request.GET.get('id')
    if noe == 'aparteman':
        posts = aparteman.objects.all()
        return render(request, 'list_view_apa.html',{"posts": posts,'f_id':f_id,'noe_f':"aparteman"})
    elif noe == 'vilae':
        posts = vilae.objects.all()
        return render(request, 'list_view_vila.html', {"posts": posts,'f_id':f_id,'noe_f':"vilae"})

def compare_post_t(request,first_noe,first_id,seconed_id):
    if first_noe == 'aparteman':
        post1 = aparteman.objects.get(id=first_id)
        post2 = aparteman.objects.get(id=seconed_id)
    elif first_noe == 'vilae':
        post1 = vilae.objects.get(id=first_id)
        post2 = vilae.objects.get(id=seconed_id)            
    context={
        'post' : post1,
        'post2' : post2,
    }
    return render(request,'compare-property-2.html',context)

    