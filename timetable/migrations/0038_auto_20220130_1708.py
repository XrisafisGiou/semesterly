# Generated by Django 3.2.11 on 2022-01-30 22:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("timetable", "0037_remove_course_vector"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="textbooklink",
            name="section",
        ),
        migrations.RemoveField(
            model_name="textbooklink",
            name="textbook",
        ),
        migrations.RemoveField(
            model_name="section",
            name="textbooks",
        ),
        migrations.DeleteModel(
            name="Textbook",
        ),
        migrations.DeleteModel(
            name="TextbookLink",
        ),
    ]
