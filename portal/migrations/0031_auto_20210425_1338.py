# Generated by Django 3.1.1 on 2021-04-25 06:38

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0030_remove_regulasi_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pengumuman',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]