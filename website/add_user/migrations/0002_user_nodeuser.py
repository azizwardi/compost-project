# Generated by Django 4.1.7 on 2023-04-25 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('add_user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='nodeuser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to='add_user.nodes'),
        ),
    ]
