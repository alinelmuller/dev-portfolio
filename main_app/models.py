from django.db import models
from django.contrib.auth.models import User

class Portfolio(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100) 
    role = models.CharField(max_length=100)
    linkedin_link = models.URLField(max_length=200)
    me_picture = models.ImageField(upload_to='me_pictures/')
    accent_color = models.CharField(max_length=7)  # Hexadecimal color
    home_picture = models.ImageField(upload_to='home_pictures/')
    personal_quotes = models.CharField(max_length=250)
    about_me = models.TextField(blank=True)
    github_link = models.URLField(max_length=200, blank=True)
    cv_pdf = models.FileField(upload_to='cvs/', blank=True)

    def edit_portfolio(self, role=None, linkedin_link=None, me_picture=None, accent_color=None, home_picture=None, personal_quotes=None):
        if role is not None:
            self.role = role
        if linkedin_link is not None:
            self.linkedin_link = linkedin_link
        if me_picture is not None:
            self.me_picture = me_picture
        if accent_color is not None:
            self.accent_color = accent_color
        if home_picture is not None:
            self.home_picture = home_picture
        if personal_quotes is not None:
            self.personal_quotes = personal_quotes
        self.save()

    def __str__(self):
        return self.role

class Skills(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=255)
    skill_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.skill_name

class Portable(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skills, on_delete=models.CASCADE)