from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('portfolios/', views.portfolio_index, name='portfolio_index'),
    path('cms/', views.create_portfolio, name='create_portfolio'),
    path('cms/<int:portfolio_id>/', views.edit_portfolio, name='edit_portfolio'),
    path('cms/<int:portfolio_id>/add_skill/', views.add_skill, name='add_skill'),
    path('cms/skill/<int:skill_id>/delete/', views.delete_skill, name='delete_skill'),
    path('users/login/', views.login_user, name='login_user'),
    path('users/register/', views.register_user, name='register_user'),
    path('users/logout/', views.logout_user, name='logout_user'),
    path('users/me/<int:portfolio_id>/', views.view_portfolio, name='view_portfolio'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)