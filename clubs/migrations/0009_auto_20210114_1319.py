# Generated by Django 3.1.4 on 2021-01-14 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0008_auto_20210114_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='publisher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clubs.student'),
        ),
    ]
