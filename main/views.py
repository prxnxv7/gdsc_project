
from django.shortcuts import render,redirect
from .forms import UserImage
import pyrebase
from django.contrib import auth

config={
    'apiKey': "AIzaSyDxKlLfPRDwT7OlTHtx1JMECMcPW_hGggk",
    'authDomain': "gdsc-b73d5.firebaseapp.com",
    'databaseURL': "https://gdsc-b73d5-default-rtdb.firebaseio.com",
    'projectId': "gdsc-b73d5",
    'storageBucket': "gdsc-b73d5.appspot.com",
    'messagingSenderId': "384913074788",
    'appId': "1:384913074788:web:476fb7354906ed5bdecd71",

}

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database

# Create your views here.
def home(request):
    return render(request, 'main/gdsc.html')

def report(request):
    return render(request,'main/report.html')

def distress(request):  
    if request.method == 'POST':  
        form = UserImage(request.POST, request.FILES)  
        if form.is_valid():  
            form.save()  
            return redirect('success')
    else:  
        form = UserImage()  
  
    return render(request, 'main/distress.html', {'form': form})  

def success(request):
    return  render(request, 'main/success.html') 

def signin(request):
    email=request.POST.get('email') 
    passw=request.POST.get('pass')
    try:
        user = authe.sign_in_with_email_and_password(email,passw) 
    except:
        message="invalid credentials"
        return  render(request, 'main/signin.html',{'messg':message})
    
    session_id=user['idToken']
    request.session['uid'] = str(session_id)
    return  render(request, 'main/distress.html',{'e':email})

def signup(request):
    name=request.POST.get('name')
    email=request.POST.get('email')
    passw=request.POST.get('pass')
    return  render(request, 'main/signup.html')


def logout(request):
    auth.logout(request)
    return  render(request, 'main/signin.html')
