# Generated by Django 2.2.16 on 2022-05-15 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20220514_1117'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
    ]
