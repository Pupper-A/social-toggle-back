# Generated by Django 3.2.13 on 2022-06-30 20:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_user_is_private'),
    ]

    operations = [
        migrations.AddField(
            model_name='follow',
            name='followed_user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='followers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='follow',
            name='user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='following', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='follow',
            unique_together={('user_id', 'followed_user_id')},
        ),
    ]
