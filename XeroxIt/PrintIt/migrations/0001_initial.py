# Generated by Django 3.2.9 on 2021-11-09 02:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('cip_address', models.CharField(blank=True, editable=False, max_length=20, null=True)),
                ('uip_address', models.CharField(blank=True, editable=False, max_length=20, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('created_by', models.ForeignKey(default=3, editable=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='userc_action', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(default=3, editable=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='useru_action', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('cip_address', models.CharField(blank=True, editable=False, max_length=20, null=True)),
                ('uip_address', models.CharField(blank=True, editable=False, max_length=20, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='')),
                ('pdf', models.FileField(blank=True, null=True, upload_to='pdf')),
                ('created_by', models.ForeignKey(default=3, editable=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='userc_document', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(default=3, editable=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='useru_document', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ExtendedUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('cip_address', models.CharField(blank=True, editable=False, max_length=20, null=True)),
                ('uip_address', models.CharField(blank=True, editable=False, max_length=20, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('phone_number', models.IntegerField(blank=True)),
                ('age', models.IntegerField(blank=True, default=0, null=True)),
                ('type', models.CharField(choices=[('CONSUMER', 'Consumer'), ('RETAILER', 'Retailer')], default='Consumer', max_length=9)),
                ('created_by', models.ForeignKey(default=3, editable=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='userc_extendeduser', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(default=3, editable=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='useru_extendeduser', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('cip_address', models.CharField(blank=True, editable=False, max_length=20, null=True)),
                ('uip_address', models.CharField(blank=True, editable=False, max_length=20, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('lat', models.DecimalField(decimal_places=6, max_digits=9)),
                ('long', models.DecimalField(decimal_places=6, max_digits=9)),
                ('addressline', models.CharField(blank=True, max_length=200, null=True)),
                ('area', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('state', models.CharField(blank=True, max_length=200, null=True)),
                ('landmark', models.CharField(blank=True, max_length=200, null=True)),
                ('created_by', models.ForeignKey(default=3, editable=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='userc_location', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(default=3, editable=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='useru_location', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('cip_address', models.CharField(blank=True, editable=False, max_length=20, null=True)),
                ('uip_address', models.CharField(blank=True, editable=False, max_length=20, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('gst', models.IntegerField(blank=True, default=0, null=True)),
                ('created_by', models.ForeignKey(default=3, editable=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='userc_node', to=settings.AUTH_USER_MODEL)),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='PrintIt.location')),
                ('updated_by', models.ForeignKey(default=3, editable=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='useru_node', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('cip_address', models.CharField(blank=True, editable=False, max_length=20, null=True)),
                ('uip_address', models.CharField(blank=True, editable=False, max_length=20, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_by', models.ForeignKey(default=3, editable=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='userc_userlocation', to=settings.AUTH_USER_MODEL)),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='PrintIt.location')),
                ('updated_by', models.ForeignKey(default=3, editable=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='useru_userlocation', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='PrintIt.extendeduser')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('cip_address', models.CharField(blank=True, editable=False, max_length=20, null=True)),
                ('uip_address', models.CharField(blank=True, editable=False, max_length=20, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('auto_id', models.AutoField(primary_key=True, serialize=False)),
                ('status_name', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('created_by', models.ForeignKey(default=3, editable=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='userc_status', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(default=3, editable=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='useru_status', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('cip_address', models.CharField(blank=True, editable=False, max_length=20, null=True)),
                ('uip_address', models.CharField(blank=True, editable=False, max_length=20, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('rating', models.IntegerField(blank=True, default=0, null=True)),
                ('comment', models.CharField(blank=True, max_length=200, null=True)),
                ('created_by', models.ForeignKey(default=3, editable=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='userc_review', to=settings.AUTH_USER_MODEL)),
                ('node', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='PrintIt.node')),
                ('updated_by', models.ForeignKey(default=3, editable=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='useru_review', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='PrintIt.extendeduser')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('cip_address', models.CharField(blank=True, editable=False, max_length=20, null=True)),
                ('uip_address', models.CharField(blank=True, editable=False, max_length=20, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('Papertype', models.CharField(choices=[('NORMAL', 'Normal'), ('HIGHQUALITY', 'Highquality')], default='No', max_length=19)),
                ('price', models.IntegerField(blank=True, default=0, null=True)),
                ('range', models.IntegerField(blank=True, default=100000, null=True)),
                ('created_by', models.ForeignKey(default=3, editable=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='userc_price', to=settings.AUTH_USER_MODEL)),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='PrintIt.location')),
                ('updated_by', models.ForeignKey(default=3, editable=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='useru_price', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrderStatusMap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('cip_address', models.CharField(blank=True, editable=False, max_length=20, null=True)),
                ('uip_address', models.CharField(blank=True, editable=False, max_length=20, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('From', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, related_name='check_from_flow', to='PrintIt.status')),
                ('action', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='PrintIt.action')),
                ('created_by', models.ForeignKey(default=3, editable=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='userc_orderstatusmap', to=settings.AUTH_USER_MODEL)),
                ('to', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='PrintIt.status')),
                ('updated_by', models.ForeignKey(default=3, editable=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='useru_orderstatusmap', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'order_status_map',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('cip_address', models.CharField(blank=True, editable=False, max_length=20, null=True)),
                ('uip_address', models.CharField(blank=True, editable=False, max_length=20, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('payment_method', models.CharField(blank=True, max_length=200, null=True)),
                ('is_paid', models.CharField(choices=[('NO', 'No'), ('YES', 'Yes'), ('PROGRESS', 'Progress')], default='No', max_length=9)),
                ('paid_at', models.DateTimeField(blank=True, null=True)),
                ('is_printed', models.CharField(choices=[('NO', 'No'), ('YES', 'Yes'), ('PROGRESS', 'Progress')], default='No', max_length=19)),
                ('price', models.IntegerField(blank=True, default=0, null=True)),
                ('From', models.IntegerField(blank=True, default=0, null=True)),
                ('status', models.IntegerField(blank=True, default=0, null=True)),
                ('created_by', models.ForeignKey(default=3, editable=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='userc_order', to=settings.AUTH_USER_MODEL)),
                ('document', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='PrintIt.document')),
                ('node_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='PrintIt.node')),
                ('updated_by', models.ForeignKey(default=3, editable=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='useru_order', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='PrintIt.extendeduser')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('type', models.CharField(choices=[('PHONE', 'Phone'), ('PRINTER', 'Printer')], default='No', max_length=19)),
                ('device_status', models.CharField(choices=[('ONLINE', 'Online'), ('OFFLINE', 'Offline')], default='No', max_length=19)),
                ('Node', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='PrintIt.node')),
                ('order_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='PrintIt.order')),
            ],
        ),
    ]
