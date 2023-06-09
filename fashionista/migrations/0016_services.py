# Generated by Django 4.1.4 on 2023-03-10 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_alter_certificates_delay'),
    ]

    operations = [
        migrations.CreateModel(
            name='services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_icon', models.TextField(blank=True, null=True)),
                ('service_heading', models.TextField(blank=True, null=True)),
                ('service_minidescrip', models.TextField(blank=True, null=True)),
                ('service_majordescrip', models.TextField(blank=True, null=True)),
                ('services_images', models.ImageField(blank=True, null=True, upload_to='media/')),
            ],
        ),
    ]
