# Generated by Django 4.1.7 on 2023-04-02 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0009_book_event_bill"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book_event",
            name="event",
            field=models.CharField(max_length=1000),
        ),
    ]
