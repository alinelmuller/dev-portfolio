from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', 'previous_migration_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=255)),
                ('skill_description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('portfolio', models.ForeignKey(on_delete=models.CASCADE, to='portfolio.Portfolio')),
            ],
        ),
        migrations.CreateModel(
            name='Portable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portfolio', models.ForeignKey(on_delete=models.CASCADE, to='portfolio.Portfolio')),
                ('skill', models.ForeignKey(on_delete=models.CASCADE, to='portfolio.Skills')),
            ],
        ),
    ]
