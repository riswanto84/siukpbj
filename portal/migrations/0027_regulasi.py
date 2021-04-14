# Generated by Django 3.1.1 on 2021-04-14 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0026_auto_20210414_0339'),
    ]

    operations = [
        migrations.CreateModel(
            name='Regulasi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('file', models.FileField(blank=True, max_length=255, null=True, upload_to='files/')),
            ],
        ),
    ]
