# Generated by Django 4.1.1 on 2022-10-22 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0003_shops_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shops',
            name='image',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
    ]