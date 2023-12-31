# Generated by Django 4.2.5 on 2023-09-14 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0003_about_menu_block_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('position', models.PositiveSmallIntegerField(unique=True)),
                ('is_visible', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Shefs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('position', models.PositiveSmallIntegerField(unique=True)),
                ('is_visible', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Shef',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('position', models.PositiveSmallIntegerField(unique=True)),
                ('is_visible', models.BooleanField(default=True)),
                ('desc', models.TextField(blank=True, max_length=1500)),
                ('photo', models.ImageField(blank=True, upload_to='chef/')),
                ('job_title', models.CharField(max_length=50, unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='shefs', to='cafe.dishcategory')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('position', models.PositiveSmallIntegerField(unique=True)),
                ('is_visible', models.BooleanField(default=True)),
                ('desc', models.TextField(blank=True, max_length=1500)),
                ('photo', models.ImageField(blank=True, upload_to='event/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='events', to='cafe.dishcategory')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
