# Generated by Django 5.0.3 on 2024-04-05 08:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("motus", "0004_alter_game_life_point_game_unique_game_per_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="ranking",
            field=models.IntegerField(default=0),
        ),
    ]