# Generated by Django 3.2.16 on 2023-01-25 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20230125_1941'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='follow',
            options={'verbose_name': 'Подписки', 'verbose_name_plural': 'Подписки'},
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.UniqueConstraint(fields=('following', 'user'), name='Follow_unique'),
        ),
    ]
