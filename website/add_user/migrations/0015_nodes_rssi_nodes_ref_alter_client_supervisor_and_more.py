# Generated by Django 4.1.7 on 2023-05-15 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supervisor_login', '0004_remove_supervisor_myclients'),
        ('add_user', '0014_remove_project_id_project_id_projet'),
    ]

    operations = [
        migrations.AddField(
            model_name='nodes',
            name='RSSI',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='nodes',
            name='ref',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='supervisor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='supervisor', to='supervisor_login.supervisor'),
        ),
        migrations.AlterField(
            model_name='project',
            name='clients',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client', to='add_user.client'),
        ),
        migrations.AlterField(
            model_name='project',
            name='nodeuser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='node', to='add_user.nodes'),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.BigIntegerField()),
                ('humidity', models.BigIntegerField()),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('node', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='add_user.nodes')),
            ],
        ),
    ]