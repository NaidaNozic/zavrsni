# Generated by Django 4.1.7 on 2023-03-14 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_assignment_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignment',
            name='student',
        ),
        migrations.AlterField(
            model_name='assignment',
            name='file_assignment',
            field=models.FileField(upload_to='assignments'),
        ),
    ]
