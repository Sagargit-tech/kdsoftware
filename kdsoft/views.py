from django.shortcuts import render
from .models import User
from .serializer import UserSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,HttpResponseRedirect
import sqlite3

# from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home(request):
    return render(request,'rr.html')


def Career(request):
    return render(request,'career.html')


def About(request):
    return render(request,'aboutus-02.html')


def php(request):
    return render(request,'php.html')


def login(request):
    import sqlite3 
    if request.method=='POST':
        email=request.POST['email']
        upass=request.POST['password']
        connection = sqlite3.connect("db.sqlite3") 
        crsr = connection.cursor() 
        crsr.execute("SELECT * FROM kdsoft_User")  
        ans = crsr.fetchall()  
        
       
        for pk in range(0,len(ans)):
            
            print(ans[pk][3])
            if ans[pk][2]==email and ans[pk][3]==upass:
                c=c+1
            else:
                c=0
        print(c)
        
        myStorage = window.localStorage;
        if c==1:
            localStorage.setItem("c", "1");
            return HttpResponseRedirect('http://127.0.0.1:8003/')
        else:
            return HttpResponseRedirect('http://127.0.0.1:8003/signup/')
            
            

    
    else:
        return render(request,'login.html')
def Signup(request):
    if request.method=='POST':
        user=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        s=User(username=user,email=email,password=password)
        s.save()

    return render(request,'signup.html')


def User_detail(request,pk):
    use=User.objects.get(id=pk) 
    serializer= UserSerializer(use)
    
    print(serializer.data)
    json_data = JSONRenderer().render(serializer.data)
    print(json_data)
    return HttpResponse(json_data,content_type='application/json')







        
