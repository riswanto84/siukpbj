# Generated by Django 3.1.1 on 2021-04-25 06:58

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0031_auto_20210425_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='berita',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='probis',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sop',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='standardokumen',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]