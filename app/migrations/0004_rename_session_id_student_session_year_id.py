# Generated by Django 4.2.14 on 2024-08-07 05:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_student'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='session_id',
            new_name='session_year_id',
        ),
    ]
