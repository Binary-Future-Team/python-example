# Generated by Django 4.2.5 on 2023-12-12 23:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0003_category_background_image_category_heading_and_more'),
        ('vendors', '0002_remove_vendor_accessories_commission_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='vendorcommission',
            unique_together={('vendor', 'subcategory')},
        ),
    ]
