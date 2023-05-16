# Generated by Django 4.2 on 2023-04-13 05:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="birthdate",
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="is_employee",
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.CharField(max_length=127, unique=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="first_name",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="user",
            name="last_name",
            field=models.CharField(max_length=50),
        ),
    ]
