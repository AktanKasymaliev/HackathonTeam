# Generated by Django 3.1.7 on 2021-02-28 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_post_user_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='user_name',
        ),
    ]
