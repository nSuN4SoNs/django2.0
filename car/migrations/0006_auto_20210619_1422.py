# Generated by Django 3.2.3 on 2021-06-19 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0005_auto_20210605_1418'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name_plural': 'Companies'},
        ),
        migrations.AlterField(
            model_name='car',
            name='car_model',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cars', to='car.carmodel'),
        ),
    ]
