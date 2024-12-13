from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Portfolio, Skills, User
from .forms import PortfolioForm, SkillsForm, UserForm

# Define the home view function
def home(request):
    # Send a simple HTML response
    return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')

# Define the about view function
def about(request):
    return render(request, 'about.html')


#---------------------------------------------------------------#


def portfolio_index(request):
    # Render the portfolios/index.html template with the portfolios data
    portfolios = Portfolio.objects.all()
    return render(request, 'portfolios/index.html', {'portfolios': portfolios})

def create_portfolio(request):
    if request.method == 'POST':
        portfolio_form = PortfolioForm(request.POST, request.FILES)
        skills_form = SkillsForm(request.POST)
        if portfolio_form.is_valid() and skills_form.is_valid():
            portfolio = portfolio_form.save()
            skill = skills_form.save(commit=False)
            skill.portfolio = portfolio
            skill.save()
            return redirect('portfolio_list')  # Change 'portfolio_list' to your desired redirect URL
    else:
        portfolio_form = PortfolioForm()
        skills_form = SkillsForm()
    return render(request, 'cms/index.html', {'form': portfolio_form, 'skills_form': skills_form})

def user_list(request):
    users = User.objects.all()
    return render(request, 'users/index.html', {'users': users})

def create_user(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('user_list')  # Change 'user_list' to your desired redirect URL
    else:
        user_form = UserForm()
    return render(request, 'users/create.html', {'form': user_form})

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_user')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('home')

#---------------------------------------------------------------#