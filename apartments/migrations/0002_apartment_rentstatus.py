# Generated by Django 4.0.2 on 2022-03-18 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='rentstatus',
            field=models.BooleanField(default=False),
        ),
    ]