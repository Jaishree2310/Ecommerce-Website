# Generated by Django 4.0.4 on 2022-06-14 11:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ecommerce_app', '0002_clothe_electronic_homeappliance_mobile_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('order_date', models.DateTimeField()),
                ('arriving_date', models.DateTimeField()),
                ('status', models.CharField(choices=[('Order Today', 'Order Today'), ('Shipped', 'Shipped'), ('Out For Delivery', 'Out For Delivery'), ('Arriving Tomorrow', 'Arriving Tomorrow'), ('Order Delivered', 'Order Delivered')], default='Order Today', max_length=100)),
                ('delivery_address', models.TextField()),
                ('amount', models.IntegerField()),
                ('quantity', models.PositiveIntegerField()),
                ('discount', models.DecimalField(decimal_places=2, max_digits=7)),
                ('payment_methos', models.CharField(choices=[('Cash', 'Cash'), ('UPI', 'UPI'), ('Net Banking', 'Net Banking')], default='Cash', max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
