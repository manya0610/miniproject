# Generated by Django 4.0.2 on 2022-03-20 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_alter_comment_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='issolved',
            field=models.BooleanField(default=False),
        ),
    ]
