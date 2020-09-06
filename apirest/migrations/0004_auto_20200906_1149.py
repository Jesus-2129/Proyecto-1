# Generated by Django 3.1 on 2020-09-06 16:49

import apirest.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('authtoken', '0002_auto_20160226_1747'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('apirest', '0003_design'),
    ]

    operations = [
        migrations.AlterField(
            model_name='design',
            name='design_file',
            field=models.FileField(default='designs_library/processing/default.jpg', null=True, upload_to=apirest.models.Design.path_and_rename, verbose_name='Diseño'),
        ),
        migrations.AlterField(
            model_name='design',
            name='design_status',
            field=models.CharField(choices=[('PROCESSING', 'Processing'), ('CONVERTED', 'Converted')], default='PROCESSING', max_length=15),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Empresa del Proyecto'),
        ),
        migrations.DeleteModel(
            name='Company',
        ),
    ]
