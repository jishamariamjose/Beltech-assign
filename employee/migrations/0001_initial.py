# Generated by Django 3.2.4 on 2021-06-21 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeSchema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EmployeeCode', models.CharField(max_length=20, unique=True)),
                ('Department', models.CharField(max_length=20)),
                ('DateCreated', models.DateTimeField()),
                ('Score', models.IntegerField()),
            ],
        ),
    ]
