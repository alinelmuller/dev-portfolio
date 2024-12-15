from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    portfolio_link = models.URLField(max_length=200, blank=True)
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    about_me = models.TextField()

    def save(self, *args, **kwargs):
        if not self.portfolio_link:
            self.portfolio_link = f"http://portfolio.dev/me/{slugify(self.user.username)}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username

class Portfolio(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100) 
    role = models.CharField(max_length=100)
    linkedin_link = models.URLField(max_length=200)
    me_picture = models.ImageField(upload_to='me_pictures/')
    accent_color = models.CharField(max_length=7)  # Hexadecimal color
    home_picture = models.ImageField(upload_to='home_pictures/')
    personal_quotes = models.CharField(max_length=250)

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

    def get_portfolio_link(self):
        return f"http://portfolio.dev/me/{slugify(self.user_id.username)}"

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

