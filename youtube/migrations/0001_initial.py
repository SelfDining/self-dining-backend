# Generated by Django 4.1.7 on 2023-05-15 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category_id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=128)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='YouTube',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_pk', models.CharField(max_length=64)),
                ('channel_id', models.CharField(max_length=64)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('thumbnails', models.URLField(blank=True, null=True)),
                ('view_count', models.IntegerField(default=0)),
                ('like_count', models.IntegerField(default=0)),
                ('published', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
