# Generated by Django 2.1.7 on 2019-11-17 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bl', '0003_auto_20191117_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='added_by',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='song',
            name='status',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
