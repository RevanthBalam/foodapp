# Generated by Django 5.2.1 on 2025-05-14 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tomato', '0009_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_image',
            field=models.ImageField(default='https://res.cloudinary.com/dtzrlblna/image/upload/v1747247647/parcel_icon_hmc6ed.png', upload_to='allimages'),
        ),
    ]
