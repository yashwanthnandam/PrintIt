# Generated by Django 3.2.9 on 2021-11-09 05:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('PrintIt', '0006_auto_20211109_0550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='created_by',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.DO_NOTHING, related_name='userc_action', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='document',
            name='created_by',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.DO_NOTHING, related_name='userc_document', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='extendeduser',
            name='created_by',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.DO_NOTHING, related_name='userc_extendeduser', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='location',
            name='created_by',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.DO_NOTHING, related_name='userc_location', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='node',
            name='created_by',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.DO_NOTHING, related_name='userc_node', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='order',
            name='created_by',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.DO_NOTHING, related_name='userc_order', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='orderstatusmap',
            name='created_by',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.DO_NOTHING, related_name='userc_orderstatusmap', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='price',
            name='created_by',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.DO_NOTHING, related_name='userc_price', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='review',
            name='created_by',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.DO_NOTHING, related_name='userc_review', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='status',
            name='created_by',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.DO_NOTHING, related_name='userc_status', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userlocation',
            name='created_by',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.DO_NOTHING, related_name='userc_userlocation', to=settings.AUTH_USER_MODEL),
        ),
    ]
