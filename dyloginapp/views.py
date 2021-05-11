from django.shortcuts import render
import datetime
# Create your views here.
def input(request):
    return render(request,'base1.html')

def output(request):
    username=request.GET['t1']
    password=str(request.GET['t2'])
    x=datetime.datetime.now()
    name="sai"
    c1=chr(64)
    y=str(name.capitalize()+c1+x.strftime("%I%M"))
    dict={'username':username,'password':password}
    if (password==y):
        return render(request,'base2.html',dict)
    else:
        z="Sorry...Please Enter Correct Password"
    dict={'username':username,'password':password,'z':z}
    return render(request,'base.html',dict)
