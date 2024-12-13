from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('portfolios/', views.portfolio_index, name='portfolio_index'),
    path('cms/', views.create_portfolio, name='create_portfolio'),
    path('users/login/', views.login_user, name='login_user'),
    path('users/register/', views.register_user, name='register_user'),
    path('users/logout/', views.logout_user, name='logout_user'),
]