# Generated by Django 5.2.1 on 2025-06-10 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='custom_id',
            field=models.CharField(max_length=10, null=True),
            preserve_default=False,
        ),
    ]
