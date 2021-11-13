# Generated by Django 3.2.9 on 2021-11-11 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PrintIt', '0013_auto_20211109_0618'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='order_id',
        ),
        migrations.AlterField(
            model_name='orderstatusmap',
            name='From',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, related_name='check_from_flow', to='PrintIt.status'),
        ),
        migrations.AlterField(
            model_name='orderstatusmap',
            name='to',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='PrintIt.status'),
        ),
        migrations.CreateModel(
            name='OrderDevice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='PrintIt.device')),
                ('order_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='PrintIt.order')),
            ],
        ),
    ]