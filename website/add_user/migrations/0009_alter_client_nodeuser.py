# Generated by Django 4.1.7 on 2023-05-05 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('add_user', '0008_rename_pays_project_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='nodeuser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client', to='add_user.nodes'),
        ),
    ]
