# Generated by Django 4.1.7 on 2023-04-17 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superspace', '0003_supervisor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supervisor',
            name='position',
        ),
        migrations.AddField(
            model_name='nodes',
            name='Description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
