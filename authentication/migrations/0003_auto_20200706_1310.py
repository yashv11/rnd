# Generated by Django 3.0.3 on 2020-07-06 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20200705_1458'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='username',
        ),
    ]
