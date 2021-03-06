from django.shortcuts import render, redirect
from .models import Fuser
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from .forms import LoginForm
from django.conf import settings
from . import forms
from django.contrib import auth
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
def register(request):

    if request.method == "GET":
        return render(request, 'register.html')
    elif request.method == "POST":
        try:
            user_id = request.POST.get('user_id', None)
            user_name = request.POST.get('user_name', None)
            cafe_name = request.POST.get('cafe_name', None)
            password = request.POST.get('password', None)
            re_password = request.POST.get('re_password', None)
            user_email = request.POST.get('user_email', None)

            res_data = {}

            if not(user_id and user_name and cafe_name and password and re_password and user_email):
                res_data['error'] = "모든 값을 입력하세요"
            elif password != re_password:
                res_data['error'] = "비밀번호가 다름"
            else:
                fuser = Fuser(
                    user_id = user_id,
                    user_name = user_name,
                    cafe_name = cafe_name,
                    password = make_password(password),
                    user_email = user_email,
                )

                fuser.save()
        except:
            return HttpResponse(status=401)
        return redirect('/fuser/login')
    

def login(request):
    if request.method == "POST":
        forms = LoginForm(request.POST)
        if forms.is_valid():
            request.session['user'] = forms.user_id
            return redirect('/')

    else:
        forms = LoginForm()
    return render(request, 'login.html', {'forms':forms})
  

  
def home(request):
    user_pk = request.session.get('user')

    if user_pk:
        fuser = Fuser.objects.get(pk=user_pk)
        return redirect('/coupon/aboutcoupon')
    return redirect("/fuser/login")

def logout(request):
    if request.session['user']:
        del request.session['user']
    return redirect('/')