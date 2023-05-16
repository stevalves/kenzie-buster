# Generated by Django 4.2 on 2023-04-14 10:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("movies", "0004_remove_movie_added_by"),
    ]

    operations = [
        migrations.AddField(
            model_name="movie",
            name="added_by",
            field=models.EmailField(default=None, max_length=254),
            preserve_default=False,
        ),
    ]
