# Generated by Django 3.0.3 on 2020-07-05 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='user_name',
            new_name='name',
        ),
    ]
