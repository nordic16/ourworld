# Generated by Django 3.2.7 on 2022-04-18 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('life', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='organism',
            name='image_primary',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='organism',
            name='image_secondary',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]
