from django.shortcuts import render, redirect, render_to_response
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . import models

def aboutPage(request):
    return render(request, 'html/aboutPage.html',{'username': auth.get_user(request).username , 'aboutPageContent': models.aboutPageContent.objects.all()})



# Create your views here.
def homePage(request):
    return render(request, 'html/homePage.html', {'username': auth.get_user(request).username , 'homePageContent': models.homePageContent.objects.all()})



# Create your views here.
def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            args['login_error'] = "пользователь не найден"
            return render_to_response('html/login.html' , args)
    else:
        return render_to_response('html/login.html' , args)

def logout(request):
    auth.logout(request)
    return redirect('/')

def register(request):
    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm()
    if request.POST:
        newuser_form = UserCreationForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = auth.authenticate(username=newuser_form.cleaned_data['username'] , password=newuser_form.cleaned_data['password2'])
            auth.login(request, newuser)
            return redirect('/')
        else:
            args['form'] = newuser_form
    return render_to_response('html/register.html', args)


def posts(request):
    return render_to_response('html/postsPage.html', {'username':auth.get_user(request).username, 'articles': models.Articles.objects.all()})

def post (request, article_id=1):
    return render_to_response('html/postPage.html', {'username':auth.get_user(request).username,'article': models.Articles.objects.get(id=article_id)})