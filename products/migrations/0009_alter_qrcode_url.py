# Generated by Django 5.0.4 on 2024-04-19 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_qrcode_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qrcode',
            name='url',
            field=models.TextField(),
        ),
    ]