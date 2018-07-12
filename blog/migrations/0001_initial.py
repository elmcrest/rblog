# Generated by Django 2.0.6 on 2018-07-12 11:53

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='_created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='_updated')),
                ('headline', models.CharField(max_length=200, verbose_name='_headline')),
                ('teaser', models.TextField(verbose_name='_teaser')),
                ('slug', models.SlugField(max_length=200, verbose_name='_slug')),
                ('in_menu', models.BooleanField(default=False, verbose_name='_in_menu')),
                ('menu_order', models.IntegerField(blank=True, null=True, verbose_name='_menu_order')),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'ordering': ['-updated'],
            },
        ),
        migrations.CreateModel(
            name='Download',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=255)),
                ('ordering', models.IntegerField(default=0)),
                ('file', models.FileField(upload_to='download/%Y/%m')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_download_set', to='blog.Article')),
            ],
            options={
                'verbose_name': '_downloaditem',
                'verbose_name_plural': '_downloaditems',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=255)),
                ('ordering', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to='images/%Y/%m')),
                ('alt', models.CharField(max_length=200)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_image_set', to='blog.Article')),
            ],
            options={
                'verbose_name': '_image',
                'verbose_name_plural': '_images',
            },
        ),
        migrations.CreateModel(
            name='RichText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=255)),
                ('ordering', models.IntegerField(default=0)),
                ('text', models.TextField(blank=True)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_richtext_set', to='blog.Article')),
            ],
            options={
                'verbose_name': '_richtext',
                'verbose_name_plural': '_richtexts',
            },
        ),
        migrations.AlterUniqueTogether(
            name='article',
            unique_together={('slug', 'created')},
        ),
    ]
