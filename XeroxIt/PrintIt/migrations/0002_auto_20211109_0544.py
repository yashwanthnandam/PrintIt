# Generated by Django 3.2.9 on 2021-11-09 05:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('PrintIt', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='status',
            name='cip_address',
        ),
        migrations.RemoveField(
            model_name='status',
            name='uip_address',
        ),
        migrations.RemoveField(
            model_name='status',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='status',
            name='updated_by',
        ),
        migrations.AlterField(
            model_name='status',
            name='created_by',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.DO_NOTHING, related_name='userc_status', to=settings.AUTH_USER_MODEL),
        ),
    ]
