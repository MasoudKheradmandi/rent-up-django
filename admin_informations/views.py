from django.shortcuts import render

# Create your views here.


def agent_list(request):
    return render(request,'agents.html',{})
    