# Generated by Django 3.2 on 2021-04-25 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='author',
            field=models.CharField(default='Konstantin Bar', max_length=255),
        ),
    ]
