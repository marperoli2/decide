# Generated by Django 2.0 on 2021-01-04 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0003_auto_20180605_0842'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='preferences',
            field=models.BooleanField(default=False, help_text='Check for creating a preference question', verbose_name='Preferences'),
        ),
    ]