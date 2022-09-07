# Generated by Django 3.1.3 on 2022-09-07 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0002_auto_20220826_1638'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='course',
        ),
        migrations.AddField(
            model_name='question',
            name='course',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='onlinecourse.course'),
        ),
    ]
