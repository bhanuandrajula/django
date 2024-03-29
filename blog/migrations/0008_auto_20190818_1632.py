# Generated by Django 2.2 on 2019-08-18 16:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20190818_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='publish_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='timestamp',
            field=models.DateTimeField(auto_now=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
