# Generated by Django 4.1.5 on 2023-01-08 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_project_github_project_preview'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='image',
        ),
    ]
