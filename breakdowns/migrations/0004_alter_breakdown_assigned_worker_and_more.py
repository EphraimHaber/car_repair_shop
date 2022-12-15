# Generated by Django 4.1.3 on 2022-12-04 09:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('breakdowns', '0003_testappointment_assigned_worker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breakdown',
            name='assigned_worker',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='breakdowns.worker'),
        ),
        migrations.AlterField(
            model_name='breakdown',
            name='car_to_repair',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='breakdowns.car'),
        ),
    ]