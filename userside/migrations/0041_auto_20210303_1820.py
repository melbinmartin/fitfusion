# Generated by Django 3.1.5 on 2021-03-03 12:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userside', '0040_auto_20210303_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback_master',
            name='ratings',
            field=models.IntegerField(help_text='Must be less than or equal to 10 <br>  10:- Highest Rating <br> 1:- Lowest Ratings', validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='user_master',
            name='id_proof',
            field=models.FileField(help_text='Any Government Approved Id(Aadhar/Driving License/PAN Card/Voter Id) <br> Must be .pdf File Only <br> Maximum Size 2MB', upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])]),
        ),
        migrations.AlterField(
            model_name='user_master',
            name='photo',
            field=models.FileField(help_text='Image File of User <br> Must of be .jpg or .png <br> Maximum Size 1MB', upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'png'])]),
        ),
        migrations.AlterField(
            model_name='workout_master',
            name='diet_chart',
            field=models.FileField(help_text='Must be pdf file <br> Maximum size:- 1MB ', upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])]),
        ),
        migrations.AlterField(
            model_name='workout_master',
            name='videos',
            field=models.FileField(help_text='Must be of .mp4 Extension <br> Maximum Size must be 300MB', upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4'])]),
        ),
        migrations.AlterField(
            model_name='workout_master',
            name='workout_schedule',
            field=models.FileField(help_text='Must be pdf file <br> Maximum size:- 1MB ', upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])]),
        ),
    ]
