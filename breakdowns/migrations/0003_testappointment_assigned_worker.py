# Generated by Django 4.1.3 on 2022-12-04 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('breakdowns', '0002_testappointment_bonus_points_on_fix_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='testappointment',
            name='assigned_worker',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='breakdowns.worker'),
        ),
    ]