# Generated by Django 4.1.7 on 2023-03-28 10:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userside', '0053_alter_user_master_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_master',
            name='photo',
            field=models.ImageField(help_text='Image File of User <br> Must of be .jpg or .png <br> Maximum Size 1MB', null=True, upload_to='media/uploads', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'png'])]),
        ),
    ]
