# Generated by Django 4.1.3 on 2022-12-04 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('breakdowns', '0005_alter_testappointment_assigned_worker_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testappointment',
            name='assigned_worker',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='breakdowns.worker'),
        ),
    ]