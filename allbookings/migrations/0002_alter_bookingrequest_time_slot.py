# Generated by Django 4.2.11 on 2024-04-07 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allbookings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingrequest',
            name='time_slot',
            field=models.CharField(choices=[('7:00 - 8:30', '7:00 - 8:30'), ('9:00 - 10:30', '9:00 - 10:30'), ('11:00 - 12:30', '11:00 - 12:30'), ('13:00 - 14:30', '13:00 - 14:30'), ('15:00 - 16:30', '15:00 - 16:30'), ('17:00 - 18:30', '17:00 - 18:30')], default='7AM', max_length=100),
        ),
    ]
