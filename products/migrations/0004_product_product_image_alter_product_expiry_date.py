# Generated by Django 5.0.4 on 2024-04-18 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_supplier_contact_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.ImageField(blank=True, null=True, upload_to='products/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='expiry_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
