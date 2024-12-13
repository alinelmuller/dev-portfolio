from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Portfolio, Skills, User
from .forms import PortfolioForm, SkillsForm, UserForm


def home(request):
    return HttpResponse('<h1>Welcome</h1>')

def about(request):
    return render(request, 'about.html')

def portfolio_index(request):
    portfolios = Portfolio.objects.all()
    return render(request, 'portfolios/index.html', {'portfolios': portfolios})

def create_portfolio(request):
    if request.method == 'POST':
        user = User.objects.get(id=request.POST['user_id'])
        name = request.POST['name']  
        role = request.POST['role']
        linkedin_link = request.POST['linkedin_link']
        me_picture = request.FILES['me_picture']
        accent_color = request.POST['accent_color']
        home_picture = request.FILES['home_picture']
        personal_quotes = request.POST['personal_quotes']

        portfolio = Portfolio(
            user_id=user,
            name=name,  
            role=role,
            linkedin_link=linkedin_link,
            me_picture=me_picture,
            accent_color=accent_color,
            home_picture=home_picture,
            personal_quotes=personal_quotes
        )
        portfolio.save()
        success_message = "Portfolio created successfully!"
        return render(request, 'cms/index.html', {
            'success_message': success_message,
            'name': name,
            'role': role,
            'linkedin_link': linkedin_link,
            'accent_color': accent_color,
            'personal_quotes': personal_quotes,
            'portfolio': portfolio
        })

    return render(request, 'cms/index.html')

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
                return redirect('create_portfolio')  
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('home')
