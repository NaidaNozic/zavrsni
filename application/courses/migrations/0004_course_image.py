# Generated by Django 4.1.7 on 2023-03-06 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_course_tutor_tutorcourse_tutor_course_studentcourse_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, default='static/img/courses_images/default.jpg', upload_to='static/img/courses_images'),
        ),
    ]
