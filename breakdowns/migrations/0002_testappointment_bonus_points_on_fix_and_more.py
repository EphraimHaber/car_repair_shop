# Generated by Django 4.1.3 on 2022-11-29 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('breakdowns', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testappointment',
            name='bonus_points_on_fix',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='testappointment',
            name='car_to_test',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='breakdowns.car'),
        ),
        migrations.AddField(
            model_name='testappointment',
            name='urgency',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='breakdown',
            name='assigned_worker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='breakdowns.worker'),
        ),
        migrations.AlterField(
            model_name='testappointment',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
