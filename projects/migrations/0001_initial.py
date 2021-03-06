# Generated by Django 4.0.1 on 2022-01-16 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('technology', models.CharField(max_length=20)),
                ('image', models.CharField(max_length=100)),
                ('cartegory', models.CharField(default='featured', max_length=20)),
                ('featured', models.BooleanField(default='True')),
                ('link', models.CharField(default='/', max_length=100)),
            ],
        ),
    ]
