# Generated by Django 4.1.7 on 2023-05-03 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('add_user', '0004_rename_user_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='add_project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_de_projet', models.CharField(max_length=200, null=True)),
                ('pays', models.CharField(max_length=100, null=True)),
                ('date_de_création', models.CharField(max_length=100, null=True)),
                ('testtest', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]