from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.db.models import Q

from app.models import *

def find_available_maids(request):
    if request.method=='POST':
        s=request.POST['s']
        g=request.POST['g']
        sr=request.POST['sr']
        hs=request.POST['hs']
        time=request.POST['ti']
        available_maids = Maid.objects.filter(Q(society=s)& Q(gender=g) & Q(service=sr) & Q(housesize=hs) & Q(availability_end__gte=time) & Q(availability_start__lte=time)).order_by('-rating')
        context = {'available_maids': available_maids}
        return render(request, 'find_available_maids.html', context)
    return HttpResponse('please first fill maid form')

def User_login(request):
    
    return render(request,'User_login.html')

def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')


def nanny(request):
    return render(request,'nanny.html')
def maid(request):
    return render(request,'maid.html')

def cook(request):
    return render(request,'cook.html')
