# Generated by Django 3.2.13 on 2022-07-01 22:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_follow_unique_together'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follow',
            old_name='followed_user_id',
            new_name='followed_user',
        ),
        migrations.RenameField(
            model_name='follow',
            old_name='user_id',
            new_name='user',
        ),
    ]