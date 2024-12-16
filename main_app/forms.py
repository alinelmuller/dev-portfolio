from django import forms
from .models import Portfolio, Skills, User

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = '__all__'
        # ...existing code...

class SkillsForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = '__all__'

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'