# Generated by Django 4.2 on 2024-03-06 02:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_rename_qunatity_orderitem_quantity'),
        ('checkout', '0003_alter_itemcart_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemcart',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itemcarts', to='core.product'),
        ),
    ]