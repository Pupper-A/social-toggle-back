# Generated by Django 3.2.13 on 2022-06-15 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='', max_length=30)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('toggle_status', models.CharField(max_length=30)),
                ('interval', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Toggle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_toggled', models.NullBooleanField()),
                ('toggled_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=80)),
                ('last_name', models.CharField(max_length=80)),
                ('username', models.CharField(max_length=80)),
                ('email', models.CharField(max_length=80)),
                ('password', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]