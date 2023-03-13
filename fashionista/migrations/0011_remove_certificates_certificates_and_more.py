# Generated by Django 4.1.7 on 2023-03-07 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_apparelproductions_apperal_products_images_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='certificates',
            name='certificates',
        ),
        migrations.AddField(
            model_name='certificates',
            name='certificate_from',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='certificates',
            name='certificates_images',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AddField(
            model_name='certificates',
            name='certificates_names',
            field=models.TextField(blank=True, null=True),
        ),
    ]
