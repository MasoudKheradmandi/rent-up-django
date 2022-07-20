from django.shortcuts import render
from .models import AdminInformation
# Create your views here.


def agent_list(request):
    agents = AdminInformation.objects.all()
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