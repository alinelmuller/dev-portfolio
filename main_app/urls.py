from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('portfolios/', views.portfolio_index, name='portfolio_index'),
    path('cms/', views.create_portfolio, name='create_portfolio'),
    path('cms/<int:portfolio_id>/', views.edit_portfolio, name='edit_portfolio'),
    path('cms/<int:portfolio_id>/add_skill/', views.add_skill, name='add_skill'),
    path('cms/skill/<int:skill_id>/delete/', views.delete_skill, name='delete_skill'),
    path('edit_skill/<int:skill_id>/', views.edit_skill, name='edit_skill'),
    path('users/login/', views.login_user, name='login_user'),
    path('users/register/', views.register_user, name='register_user'),
    path('users/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('users/me/<int:portfolio_id>/', views.view_portfolio, name='view_portfolio'),
    path('confirm_email/', views.confirm_email, name='confirm_email'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)