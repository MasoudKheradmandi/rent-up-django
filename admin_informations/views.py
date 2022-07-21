from django.shortcuts import render
from .models import AdminInformation 
# Create your views here.


def agent_list(request):
    agents = AdminInformation.objects.all()
    print(request.GET.get('next'))
    context = {
        "agents" : agents ,
    }
    return render(request,'agents.html',context)
    
def agent_detail(request,id):
    agent = AdminInformation.objects.get(id=id)
    context = {
        'agent' : agent,
    }
    return render(request,'agent-page.html',context)


def dashboard(request):
    return render(request,'dashboard.html',{})



def MyProperty(request):
    ip_address = request.user.ip_address
    return render(request,'my-property.html',{})