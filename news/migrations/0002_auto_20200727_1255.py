# Generated by Django 3.0.8 on 2020-07-27 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='headline',
            name='image',
        ),
        migrations.AddField(
            model_name='headline',
            name='text',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='headline',
            name='url',
            field=models.TextField(default=''),
        ),
    ]
