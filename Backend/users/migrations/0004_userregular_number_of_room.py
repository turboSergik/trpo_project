# Generated by Django 3.2.9 on 2021-12-07 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20211206_0942'),
    ]

    operations = [
        migrations.AddField(
            model_name='userregular',
            name='number_of_room',
            field=models.CharField(default='', max_length=30),
        ),
    ]
