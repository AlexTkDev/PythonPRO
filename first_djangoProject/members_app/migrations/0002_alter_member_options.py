# Generated by Django 5.0.6 on 2024-05-21 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("members_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="member",
            options={
                "verbose_name": "введённый текст",
                "verbose_name_plural": "всё что мы ввели:",
            },
        ),
    ]