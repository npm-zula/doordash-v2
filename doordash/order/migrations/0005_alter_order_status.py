# Generated by Django 3.2 on 2023-09-03 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Ordered', 'Orderd'), ('Paid', 'Paid'), ('Cancelled', 'Cancelled'), ('Completed', 'Completed')], default='Ordered', max_length=10),
        ),
    ]
