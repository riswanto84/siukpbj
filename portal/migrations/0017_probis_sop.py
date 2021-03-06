# Generated by Django 3.1.1 on 2021-04-13 03:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0016_strukturorganisasi'),
    ]

    operations = [
        migrations.CreateModel(
            name='Probis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('file', models.FileField(blank=True, max_length=255, null=True, upload_to='files/')),
            ],
        ),
        migrations.CreateModel(
            name='SOP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('file', models.FileField(blank=True, max_length=255, null=True, upload_to='files/')),
                ('probis', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='portal.probis')),
            ],
        ),
    ]
