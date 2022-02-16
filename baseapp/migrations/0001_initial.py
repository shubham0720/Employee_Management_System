# Generated by Django 4.0.2 on 2022-02-16 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeDataManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.IntegerField()),
                ('employee_name', models.CharField(max_length=20)),
                ('employee_age', models.IntegerField()),
                ('employee_addr', models.CharField(max_length=100)),
                ('employee_dept', models.CharField(max_length=20)),
                ('employee_start_date', models.DateField()),
            ],
        ),
    ]
