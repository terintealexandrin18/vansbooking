# Generated by Django 4.2.11 on 2024-04-11 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_remove_homepage_featured_image_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='home_page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.homepage'),
        ),
    ]
