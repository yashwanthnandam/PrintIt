# Generated by Django 3.2.9 on 2021-11-09 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PrintIt', '0012_rename_node_id_order_node'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderstatusmap',
            name='From',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='check_from_flow', to='PrintIt.status'),
        ),
        migrations.AlterField(
            model_name='orderstatusmap',
            name='to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='PrintIt.status'),
        ),
    ]
