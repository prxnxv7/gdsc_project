# Generated by Django 4.1.7 on 2023-03-29 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_report_number_report_phone'),
    ]

    operations = [
        migrations.DeleteModel(
            name='report',
        ),
        migrations.RemoveField(
            model_name='uploadimage',
            name='caption',
        ),
        migrations.AddField(
            model_name='uploadimage',
            name='comment',
            field=models.TextField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='uploadimage',
            name='created',
            field=models.DateTimeField(auto_created=True, null=True),
        ),
        migrations.AddField(
            model_name='uploadimage',
            name='phone',
            field=models.CharField(max_length=10, null=True),
        ),
    ]