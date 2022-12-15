from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def counter(request):
    
    text = request.POST['words']
    number_of_words = len(text.split())
    return render(request, 'counter.html', {'number':number_of_words})


def signup(request):
    
    if request.method == 'POST':
        username  = request.POST['username']
        email  = request.POST['email']
        password  = request.POST['password']
        password2  = request.POST['password2']
        
        if password == password2:
            if User.objects.filter(email=email).exists():    #old_user
                messages.info(request, 'Email already registered')
                return redirect('signup')
            
            elif User.objects.filter(username=username).exists():  #old_user
                messages.info(request, 'Username already registered')
                return redirect('signup')
            
            else:   #new_user
                user = User.objects.create_user(username=username, email=email, password=password) 
                user.save();
                return redirect('login')
        else:
            messages.info(request, "Passwords does not match")
            return redirect('signup')
        
    else:
        return render(request, 'signup.html')  


def login(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Incorrect credentails')
            return redirect('login')
    else:
        return render(request, 'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect("/")