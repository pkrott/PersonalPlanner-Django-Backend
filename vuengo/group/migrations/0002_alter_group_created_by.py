# Generated by Django 4.0.6 on 2022-08-02 01:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('group', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_taskG', to=settings.AUTH_USER_MODEL),
        ),
    ]