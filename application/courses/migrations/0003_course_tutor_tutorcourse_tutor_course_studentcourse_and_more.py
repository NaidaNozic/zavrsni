# Generated by Django 4.1.7 on 2023-03-06 19:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('summary', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='Tutor', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TutorCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_name_tutor', to='courses.course')),
                ('tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tutor_name', to='courses.tutor')),
            ],
            options={
                'unique_together': {('course', 'tutor')},
            },
        ),
        migrations.AddField(
            model_name='tutor',
            name='course',
            field=models.ManyToManyField(through='courses.TutorCourse', to='courses.course'),
        ),
        migrations.CreateModel(
            name='StudentCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_name_student', to='courses.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_name', to='courses.student')),
            ],
            options={
                'unique_together': {('course', 'student')},
            },
        ),
        migrations.AddField(
            model_name='student',
            name='course',
            field=models.ManyToManyField(through='courses.StudentCourse', to='courses.course'),
        ),
    ]
