# Generated by Django 3.0.3 on 2020-09-20 07:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CorrectChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correct_choice', models.CharField(max_length=1500)),
                ('answer', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='question.Question')),
            ],
        ),
    ]
