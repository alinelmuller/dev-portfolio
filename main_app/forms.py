from django import forms
from .models import Portfolio, Skills, User

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = [
            'name', 'role', 'about_me', 'github_link', 'cv_pdf',
            'linkedin_link', 'personal_quotes', 'accent_color',
            'home_picture', 'me_picture'
        ]

class SkillsForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = '__all__'

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'