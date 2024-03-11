# Generated by Django 4.2 on 2024-03-10 00:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_key', models.CharField(db_index=True, max_length=40, verbose_name='Chave do Carrinho')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Quantidade')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Preço')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado Em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado Em')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itemcarts', to='core.product')),
            ],
            options={
                'verbose_name': 'Item do carrinho',
                'verbose_name_plural': 'Itens dos carrinhos',
                'unique_together': {('cart_key', 'product')},
            },
        ),
    ]
