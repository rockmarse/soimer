# Generated by Django 4.1.7 on 2023-03-06 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_delete_makeadiff_delete_whypakistan_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='whywe',
            name='makeadiff_quote',
        ),
        migrations.AddField(
            model_name='whywe',
            name='makeadiff_img',
            field=models.ImageField(blank=True, max_length=250, null=True, upload_to='media/'),
        ),
        migrations.AddField(
            model_name='whywe',
            name='organization_img',
            field=models.ImageField(blank=True, max_length=250, null=True, upload_to='media/'),
        ),
    ]
