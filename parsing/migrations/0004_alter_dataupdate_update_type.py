# Generated by Django 3.2.11 on 2022-01-30 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("parsing", "0003_auto_20170910_2155"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dataupdate",
            name="update_type",
            field=models.CharField(
                choices=[
                    ("C", "courses"),
                    ("E", "evaluations"),
                    ("M", "miscellaneous"),
                ],
                default="M",
                max_length=1,
            ),
        ),
    ]
