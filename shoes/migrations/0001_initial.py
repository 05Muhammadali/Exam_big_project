# Generated by Django 4.2 on 2023-04-20 16:03

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
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Sneakers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('character', models.TextField()),
                ('price_type', models.CharField(choices=[("so'm", "so'm"), ('rub', 'rub'), ('$', '$')], default="so'm", max_length=10)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='')),
                ('types', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoes.category')),
            ],
        ),
    ]