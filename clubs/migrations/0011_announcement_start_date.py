# Generated by Django 3.1.4 on 2021-01-14 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0010_auto_20210114_1320'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='start_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]