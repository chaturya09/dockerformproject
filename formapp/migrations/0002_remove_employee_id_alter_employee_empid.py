# Generated by Django 5.1.1 on 2024-10-21 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='id',
        ),
        migrations.AlterField(
            model_name='employee',
            name='empid',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
