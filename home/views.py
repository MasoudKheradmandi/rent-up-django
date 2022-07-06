from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request,'index.html',{})


def ListView(request):
	return render(request,'list_view.html',{})

def detailview(request):
	return render(request,'detail.html',{})