from django.shortcuts import render
from App1 import forms
# Create your views here.
def emp(request):
    form=forms.empform()
    dct={'form':form}
    return render(request,'App1/home.html',dct)

def thanks(request):
    return render(request,'App1/thanks.html')
