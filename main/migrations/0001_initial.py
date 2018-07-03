# Generated by Django 2.0.6 on 2018-07-01 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='original_images')),
                ('caption', models.CharField(max_length=200, verbose_name='_caption')),
            ],
        ),
    ]
