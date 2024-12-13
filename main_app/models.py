from django.db import models
from django.contrib.auth.models import User

class Portfolio(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=100)
    linkedin_link = models.URLField(max_length=200)
    me_picture = models.ImageField(upload_to='me_pictures/')
    accent_color = models.CharField(max_length=7)  # Hexadecimal color
    home_picture = models.ImageField(upload_to='home_pictures/')
    personal_quotes = models.CharField(max_length=250)

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

# Remove the custom User model if it exists
# class User(models.Model):
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=128)
#     name = models.CharField(max_length=255)

#     def __str__(self):
#         return self.email