# Generated by Django 4.1.2 on 2022-10-24 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0004_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='product-files/'),
        ),
    ]
