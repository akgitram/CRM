# Generated by Django 3.2.12 on 2022-11-30 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0015_attendancerange'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attendanceclass',
            options={'verbose_name': 'Attendance', 'verbose_name_plural': 'Attendance'},
        ),
        migrations.AlterField(
            model_name='assigntime',
            name='period',
            field=models.CharField(choices=[('10:00 - 10:45', '10:00 - 10:45'), ('10:45 - 11:30', '10:45 - 11:30'), ('11:30 - 12:15', '11:30 - 12:15'), ('12:15 - 1:15', '12:15 - 1:15'), ('1:15 - 2;00', '1:15 - 2:00'), ('2:00 - 2:45', '2:00 - 2:45'), ('2:45 - 3:30', '2:45 - 3:30'), ('3:30 - 4:15', '3:30 - 4:15'), ('4:15 - 5:00', '4:15 - 5:00')], default='11:00 - 11:50', max_length=50),
        ),
        migrations.AlterField(
            model_name='marks',
            name='name',
            field=models.CharField(choices=[('Internal test 1', 'Internal test 1'), ('Internal test 2', 'Internal test 2'), ('Internal test 3', 'Internal test 3'), ('Semester End Exam', 'Semester End Exam')], default='Internal test 1', max_length=50),
        ),
        migrations.AlterField(
            model_name='marksclass',
            name='name',
            field=models.CharField(choices=[('Internal test 1', 'Internal test 1'), ('Internal test 2', 'Internal test 2'), ('Internal test 3', 'Internal test 3'), ('Semester End Exam', 'Semester End Exam')], default='Internal test 1', max_length=50),
        ),
    ]