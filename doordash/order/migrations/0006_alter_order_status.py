# Generated by Django 3.2 on 2023-09-04 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Ordered', 'ORDERED'), ('Paid', 'PAID'), ('Cancelled', 'CANCELLED'), ('Completed', 'COMPLETED')], default='Ordered', max_length=10),
        ),
    ]
