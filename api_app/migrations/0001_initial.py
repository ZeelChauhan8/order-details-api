# Generated by Django 4.0.3 on 2022-03-11 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('i_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('etd', models.TimeField()),
                ('d_address', models.TextField()),
                ('b_address', models.TextField()),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cust_fk', to='api_app.customers')),
            ],
        ),
        migrations.CreateModel(
            name='Order_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='item_fk', to='api_app.items')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='order_fk', to='api_app.orders')),
            ],
        ),
        migrations.CreateModel(
            name='Delayed_orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_time', models.TimeField()),
                ('etd', models.TimeField()),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='orders_fk', to='api_app.orders')),
            ],
        ),
    ]