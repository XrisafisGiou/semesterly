# Generated by Django 3.2.18 on 2023-04-08 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("timetable", "0039_auto_20230303_1640"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="school",
            field=models.CharField(max_length=100),
        ),
    ]
