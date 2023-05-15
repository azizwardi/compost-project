# Generated by Django 4.1.7 on 2023-05-10 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('add_user', '0012_remove_client_nodeuser_project_nodeuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='project',
        ),
        migrations.AddField(
            model_name='project',
            name='clients',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project', to='add_user.client'),
        ),
        migrations.AlterField(
            model_name='project',
            name='nodeuser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project', to='add_user.nodes'),
        ),
    ]
