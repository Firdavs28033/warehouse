# Generated by Django 5.0.4 on 2024-04-24 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_user_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, default='change me', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, default='change me', max_length=150),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, default='change me', max_length=150),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, default='change me', max_length=15, null=True),
        ),
    ]
