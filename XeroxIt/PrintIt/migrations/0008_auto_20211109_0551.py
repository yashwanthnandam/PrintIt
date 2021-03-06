# Generated by Django 3.2.9 on 2021-11-09 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PrintIt', '0007_auto_20211109_0551'),
    ]

    operations = [
        migrations.AddField(
            model_name='action',
            name='cip_address',
            field=models.CharField(blank=True, editable=False, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='action',
            name='uip_address',
            field=models.CharField(blank=True, editable=False, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='document',
            name='cip_address',
            field=models.CharField(blank=True, editable=False, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='document',
            name='uip_address',
            field=models.CharField(blank=True, editable=False, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='extendeduser',
            name='cip_address',
            field=models.CharField(blank=True, editable=False, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='extendeduser',
            name='uip_address',
            field=models.CharField(blank=True, editable=False, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='cip_address',
            field=models.CharField(blank=True, editable=False, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='uip_address',
            field=models.CharField(blank=True, editable=False, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='node',
            name='cip_address',
            field=models.CharField(blank=True, editable=False, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='node',
            name='uip_address',
            field=models.CharField(blank=True, editable=False, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='cip_address',
            field=models.CharField(blank=True, editable=False, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='uip_address',
            field=models.CharField(blank=True, editable=False, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='orderstatusmap',
            name='cip_address',
            field=models.CharField(blank=True, editable=False, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='orderstatusmap',
            name='uip_address',
            field=models.CharField(blank=True, editable=False, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='price',
            name='cip_address',
            field=models.CharField(blank=True, editable=False, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='price',
            name='uip_address',
            field=models.CharField(blank=True, editable=False, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='cip_address',
            field=models.CharField(blank=True, editable=False, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='uip_address',
            field=models.CharField(blank=True, editable=False, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='status',
            name='cip_address',
            field=models.CharField(blank=True, editable=False, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='status',
            name='uip_address',
            field=models.CharField(blank=True, editable=False, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='userlocation',
            name='cip_address',
            field=models.CharField(blank=True, editable=False, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='userlocation',
            name='uip_address',
            field=models.CharField(blank=True, editable=False, max_length=20, null=True),
        ),
    ]
