# Generated by Django 3.1.1 on 2021-04-12 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0008_beritafiles'),
    ]

    operations = [
        migrations.CreateModel(
            name='TautanAplikasi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=500)),
                ('thumbnailImage', models.ImageField(upload_to='')),
            ],
        ),
    ]
