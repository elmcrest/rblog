# Generated by Django 2.0.6 on 2018-07-09 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180709_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='menu_order',
            field=models.IntegerField(blank=True, null=True, verbose_name='_menu_order'),
        ),
    ]
