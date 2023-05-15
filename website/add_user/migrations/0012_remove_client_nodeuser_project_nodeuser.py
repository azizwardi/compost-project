# Generated by Django 4.1.7 on 2023-05-09 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('add_user', '0011_client_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='nodeuser',
        ),
        migrations.AddField(
            model_name='project',
            name='nodeuser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client', to='add_user.nodes'),
        ),
    ]