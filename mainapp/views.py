from django.shortcuts import render
from .forms import userregistrationform

# Create your views here.
def index(request):
    return render(request,"index.html")

def registrations(request):
    fm=userregistrationform()
    return render(request,"registrations.html",{'form':fm})
