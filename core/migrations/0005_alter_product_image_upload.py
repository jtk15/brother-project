# Generated by Django 4.2 on 2024-02-21 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_product_image_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image_upload',
            field=models.ImageField(blank=True, upload_to='core/static/image/'),
        ),
    ]
