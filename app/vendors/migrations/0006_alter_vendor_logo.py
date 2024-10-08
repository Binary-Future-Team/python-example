# Generated by Django 4.2.5 on 2024-02-13 22:15

import core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0005_vendorcommission_global_commission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='logo',
            field=models.ImageField(upload_to='vendor/%Y/%m/%d/', validators=[core.validators.ImageMaxSizeValidator(268, 268)]),
        ),
    ]
