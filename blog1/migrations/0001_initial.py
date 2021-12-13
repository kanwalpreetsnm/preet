# Generated by Django 3.2.7 on 2021-10-28 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('slug', models.SlugField(max_length=70, unique=True)),
                ('img', models.ImageField(upload_to='categorypics')),
            ],
        ),
        migrations.CreateModel(
            name='POST',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('desc', models.TextField()),
                ('img', models.ImageField(upload_to='postimage')),
                ('slug', models.CharField(max_length=100, unique=True)),
                ('author', models.CharField(max_length=40)),
                ('timestamp', models.DateTimeField(blank=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog1.category')),
            ],
        ),
    ]