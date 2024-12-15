from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth.models import User
import json
import logging

from .models import Portfolio, Skills, User, UserProfile
from .forms import PortfolioForm, SkillsForm, UserForm, UserProfileForm

logger = logging.getLogger(__name__)

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
            try:
                portfolio = form.save(commit=False)
                portfolio.user_id = request.user
                portfolio.save()
                messages.success(request, "Portfolio created successfully!")
                return redirect('edit_portfolio', portfolio_id=portfolio.id)
            except Exception as e:
                logger.error(f"Error creating portfolio: {e}")
                messages.error(request, "Error creating portfolio.")
        else:
            logger.error(f"Form errors: {form.errors}")
            messages.error(request, "Error creating portfolio.")
    else:
        form = PortfolioForm()
    return render(request, 'cms/index.html', {'form': form})

def view_portfolio(request, portfolio_id):
    portfolio = get_object_or_404(Portfolio, id=portfolio_id)
    portfolio_link = portfolio.get_portfolio_link()
    return render(request, 'users/me.html', {'portfolio': portfolio, 'portfolio_link': portfolio_link})

def edit_portfolio(request, portfolio_id):
    portfolio = get_object_or_404(Portfolio, id=portfolio_id)
    user_profile = get_object_or_404(UserProfile, user=portfolio.user_id)
    if request.method == 'POST':
        form = PortfolioForm(request.POST, request.FILES, instance=portfolio)
        profile_form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid() and profile_form.is_valid():
            form.save()
            profile_form.save()
            messages.success(request, "Portfolio updated successfully!")
            return redirect('view_portfolio', portfolio_id=portfolio.id)
        else:
            messages.error(request, "Error updating portfolio.")
    else:
        form = PortfolioForm(instance=portfolio)
        profile_form = UserProfileForm(instance=user_profile)
    return render(request, 'cms/index.html', {'form': form, 'profile_form': profile_form, 'portfolio': portfolio})

def add_skill(request, portfolio_id):
    portfolio = get_object_or_404(Portfolio, id=portfolio_id)
    if request.method == 'POST':
        form = SkillsForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.portfolio = portfolio
            skill.save()
            messages.success(request, "Skill added successfully!")
        else:
            messages.error(request, "Error adding skill.")
    return redirect('edit_portfolio', portfolio_id=portfolio.id)

def delete_skill(request, skill_id):
    skill = get_object_or_404(Skills, id=skill_id)
    portfolio_id = skill.portfolio.id
    skill.delete()
    messages.success(request, "Skill deleted successfully!")
    return redirect('edit_portfolio', portfolio_id=portfolio_id)

def edit_skill(request, skill_id):
    skill = get_object_or_404(Skills, id=skill_id)
    portfolio_id = skill.portfolio.id
    if request.method == 'POST':
        form = SkillsForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, "Skill updated successfully!")
            return redirect('edit_portfolio', portfolio_id=portfolio_id)
        else:
            messages.error(request, "Error updating skill.")
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
            messages.success(request, "User created successfully!")
            return redirect('user_list')
        else:
            messages.error(request, "Error creating user.")
    else:
        user_form = UserForm()
    return render(request, 'users/create.html', {'form': user_form})

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(request, "Registration successful!")
            return redirect('login_user')
        else:
            messages.error(request, "Error during registration.")
    else:
        form = UserCreationForm()
        profile_form = UserProfileForm()
    return render(request, 'users/register.html', {'form': form, 'profile_form': profile_form})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login successful!")
                return redirect('create_portfolio')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def logout_user(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('home')

def confirm_email(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        user_exists = User.objects.filter(email=email).exists()
        return JsonResponse({'valid': user_exists})
    return JsonResponse({'valid': False})

def cms_index(request, portfolio_id):
    portfolio = get_object_or_404(Portfolio, id=portfolio_id)
    return render(request, 'cms/index.html', {'portfolio': portfolio})