# Generated by Django 4.2.2 on 2023-09-06 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invista_me', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='investimento',
            name='niel',
            field=models.IntegerField(default=1),
        ),
    ]
