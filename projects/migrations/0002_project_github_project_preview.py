# Generated by Django 4.1.5 on 2023-01-07 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='github',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='preview',
            field=models.URLField(blank=True),
        ),
    ]