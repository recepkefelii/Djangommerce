# Generated by Django 4.1.1 on 2022-10-23 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_delete_subcategories'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categories',
            old_name='created_by',
            new_name='auth',
        ),
        migrations.RenameField(
            model_name='categories',
            old_name='created',
            new_name='date',
        ),
    ]
