# Generated by Django 4.1.7 on 2023-03-07 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_rename_apparelproduction_apparelproductions'),
    ]

    operations = [
        migrations.CreateModel(
            name='packagingandsampling',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('packagingandsampling_halfheading', models.TextField(blank=True, null=True)),
                ('packagingandsampling_paragraph', models.TextField(blank=True, null=True)),
                ('packagingandsampling_secondhalfheading', models.ImageField(blank=True, null=True, upload_to='media/')),
            ],
        ),
        migrations.CreateModel(
            name='shipping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shippinghalfheading', models.TextField(blank=True, null=True)),
                ('shipping_paragraph', models.TextField(blank=True, null=True)),
                ('shipping_secondhalfheading', models.ImageField(blank=True, null=True, upload_to='media/')),
            ],
        ),
        migrations.DeleteModel(
            name='packagingandshipping',
        ),
        migrations.DeleteModel(
            name='sustainablefashion',
        ),
        migrations.RenameField(
            model_name='apparelproductions',
            old_name='BulkProduction_paragraph',
            new_name='apperal_products_halfheading',
        ),
        migrations.RenameField(
            model_name='apparelproductions',
            old_name='CostingandPlacement_paragraph',
            new_name='apperal_products_paragraph',
        ),
        migrations.RenameField(
            model_name='product_development',
            old_name='sampling_paragraph',
            new_name='product_development_halfheading',
        ),
        migrations.RenameField(
            model_name='whywe',
            old_name='makeadiff_paragraph',
            new_name='whywe_halfheading',
        ),
        migrations.RemoveField(
            model_name='apparelproductions',
            name='BulkProduction',
        ),
        migrations.RemoveField(
            model_name='apparelproductions',
            name='CostingandPlacement',
        ),
        migrations.RemoveField(
            model_name='apparelproductions',
            name='GarmentTesting',
        ),
        migrations.RemoveField(
            model_name='apparelproductions',
            name='GarmentTesting_paragraph',
        ),
        migrations.RemoveField(
            model_name='apparelproductions',
            name='PrintandEmbroidery',
        ),
        migrations.RemoveField(
            model_name='apparelproductions',
            name='PrintandEmbroidery_paragraph',
        ),
        migrations.RemoveField(
            model_name='apparelproductions',
            name='QualityAssurance',
        ),
        migrations.RemoveField(
            model_name='apparelproductions',
            name='QualityAssurance_paragraph',
        ),
        migrations.RemoveField(
            model_name='apparelproductions',
            name='TrimSourcing',
        ),
        migrations.RemoveField(
            model_name='apparelproductions',
            name='TrimSourcing_paragraph',
        ),
        migrations.RemoveField(
            model_name='product_development',
            name='product_development',
        ),
        migrations.RemoveField(
            model_name='product_development',
            name='sampling',
        ),
        migrations.RemoveField(
            model_name='whywe',
            name='makeadiff_img',
        ),
        migrations.RemoveField(
            model_name='whywe',
            name='organization_if_any',
        ),
        migrations.RemoveField(
            model_name='whywe',
            name='organization_img',
        ),
        migrations.RemoveField(
            model_name='whywe',
            name='whypakistan_img',
        ),
        migrations.RemoveField(
            model_name='whywe',
            name='whypakistan_paragraph',
        ),
        migrations.RemoveField(
            model_name='whywe',
            name='whywe_img',
        ),
        migrations.AddField(
            model_name='apparelproductions',
            name='apperal_products_secondhalfheading',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AddField(
            model_name='product_development',
            name='product_development_secondhalfheading',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AddField(
            model_name='whywe',
            name='whywe_secondhalfheading',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
