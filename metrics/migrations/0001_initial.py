# Generated by Django 2.2.1 on 2019-05-21 21:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InventoryProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_qty_purchased', models.IntegerField(default=0)),
                ('total_qty_sold', models.IntegerField(default=0)),
                ('total_qty_expired', models.IntegerField(default=0)),
                ('total_qty_in_stock', models.IntegerField(default=0)),
                ('profit', models.FloatField(default=0.0)),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='product.Product')),
            ],
        ),
    ]