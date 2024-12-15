from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth.models import User
import json

from .models import Portfolio, Skills, User
from .forms import PortfolioForm, SkillsForm, UserForm


def home(request):
    return render(request, 'about.html')

def about(request):
    return render(request, 'about.html')

def portfolio_index(request):
    portfolios = Portfolio.objects.all()
    return render(request, 'portfolios/index.html', {'portfolios': portfolios})

def create_portfolio(request):
    if request.method == 'POST':
        form = PortfolioForm(request.POST, request.FILES)
        if form.is_valid():
            portfolio = form.save()
            success_message = "Portfolio created successfully!"
            return render(request, 'cms/index.html', {'success_message': success_message, 'form': form, 'portfolio': portfolio})
    else:
        form = PortfolioForm()
    return render(request, 'cms/index.html', {'form': form})

def view_portfolio(request, portfolio_id):
    portfolio = get_object_or_404(Portfolio, id=portfolio_id)
    return render(request, 'users/me.html', {'portfolio': portfolio})

def edit_portfolio(request, portfolio_id):
    portfolio = get_object_or_404(Portfolio, id=portfolio_id)
    if request.method == 'POST':
        form = PortfolioForm(request.POST, request.FILES, instance=portfolio)
        if form.is_valid():
            form.save()
            return redirect('view_portfolio', portfolio_id=portfolio.id)
    else:
        form = PortfolioForm(instance=portfolio)
    return render(request, 'cms/index.html', {'form': form, 'portfolio': portfolio})

def add_skill(request, portfolio_id):
    portfolio = get_object_or_404(Portfolio, id=portfolio_id)
    if request.method == 'POST':
        skill_name = request.POST['skill_name']
        skill_description = request.POST['skill_description']
        skill = Skills(portfolio=portfolio, skill_name=skill_name, skill_description=skill_description)
        skill.save()
        return redirect('edit_portfolio', portfolio_id=portfolio.id)

def delete_skill(request, skill_id):
    skill = get_object_or_404(Skills, id=skill_id)
    portfolio_id = skill.portfolio.id
    skill.delete()
    return redirect('edit_portfolio', portfolio_id=portfolio_id)

def edit_skill(request, skill_id):
    skill = get_object_or_404(Skills, id=skill_id)
    portfolio_id = skill.portfolio.id
    if request.method == 'POST':
        form = SkillsForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            return redirect('edit_portfolio', portfolio_id=portfolio_id)
    else:
        form = SkillsForm(instance=skill)
    return render(request, 'cms/index.html', {'form': form, 'portfolio': skill.portfolio})

def user_list(request):
    users = User.objects.all()
    return render(request, 'users/index.html', {'users': users})

def create_user(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('user_list') 
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
                return redirect('create_portfolio')  
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('home')

def confirm_email(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        user = User.objects.filter(email=email).exists()
        return JsonResponse({'valid': user})
    return JsonResponse({'valid': False})