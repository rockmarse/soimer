# Generated by Django 4.1.7 on 2023-03-07 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_packagingandsampling_shipping_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='apparelproductions',
            name='apperal_products_images',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AddField(
            model_name='packagingandsampling',
            name='packagingandsampling_images',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AddField(
            model_name='product_development',
            name='product_development_images',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AddField(
            model_name='shipping',
            name='shipping_images',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AddField(
            model_name='whywe',
            name='whywe_images',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='apparelproductions',
            name='apperal_products_secondhalfheading',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='packagingandsampling',
            name='packagingandsampling_secondhalfheading',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product_development',
            name='product_development_secondhalfheading',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='shipping',
            name='shipping_secondhalfheading',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='whywe',
            name='whywe_secondhalfheading',
            field=models.TextField(blank=True, null=True),
        ),
    ]