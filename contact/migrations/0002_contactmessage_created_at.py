# Generated by Django 4.2.11 on 2024-04-10 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactmessage',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
