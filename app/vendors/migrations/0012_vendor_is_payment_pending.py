# Generated by Django 4.2.5 on 2024-08-12 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0011_vendor_is_send_receipt'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='is_payment_pending',
            field=models.BooleanField(default=False, verbose_name='Payment Pending'),
        ),
    ]
