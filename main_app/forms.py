from django import forms
from .models import Portfolio, Skills, User, UserProfile

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = '__all__'

class SkillsForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = '__all__'

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'role', 'about_me']

