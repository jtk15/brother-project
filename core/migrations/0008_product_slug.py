# Generated by Django 4.2 on 2024-02-23 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.TextField(blank=True, max_length=200),
        ),
    ]