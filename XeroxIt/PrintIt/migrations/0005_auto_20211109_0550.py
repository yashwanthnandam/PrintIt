# Generated by Django 3.2.9 on 2021-11-09 05:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PrintIt', '0004_auto_20211109_0546'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='action',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='document',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='extendeduser',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='location',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='node',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='order',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='orderstatusmap',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='price',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='review',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='status',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='userlocation',
            name='updated_at',
        ),
    ]