# Generated by Django 4.1.4 on 2022-12-17 13:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("articles", "0003_alter_postimages_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2022, 12, 17, 13, 29, 55, 132649, tzinfo=datetime.timezone.utc
                ),
                editable=False,
            ),
        ),
    ]
