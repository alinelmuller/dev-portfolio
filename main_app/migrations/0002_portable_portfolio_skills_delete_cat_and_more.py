# Generated by Django 5.1.4 on 2024-12-13 17:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Portable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('breed', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=250)),
                ('age', models.IntegerField()),
                ('role', models.CharField(max_length=100)),
                ('linkedin_link', models.URLField()),
                ('me_picture', models.ImageField(upload_to='me_pictures/')),
                ('accent_color', models.CharField(max_length=7)),
                ('home_picture', models.ImageField(upload_to='home_pictures/')),
                ('personal_quotes', models.CharField(max_length=250)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=255)),
                ('skill_description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.portfolio')),
            ],
        ),
        migrations.DeleteModel(
            name='Cat',
        ),
        migrations.AddField(
            model_name='portable',
            name='portfolio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.portfolio'),
        ),
        migrations.AddField(
            model_name='portable',
            name='skill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.skills'),
        ),
    ]
