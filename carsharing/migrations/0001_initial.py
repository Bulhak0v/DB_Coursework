# Generated by Django 5.1.3 on 2024-11-06 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(choices=[('reserved', 'Reserved'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], default='reserved', max_length=10)),
            ],
            options={
                'db_table': 'booking',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('car_id', models.AutoField(primary_key=True, serialize=False)),
                ('car_type', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=30)),
                ('license_plate', models.CharField(max_length=15)),
                ('release_year', models.IntegerField()),
                ('price_per_day', models.IntegerField()),
                ('car_status', models.BooleanField()),
            ],
            options={
                'db_table': 'Car',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=20)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('driver_license', models.CharField(max_length=9)),
            ],
            options={
                'db_table': 'User',
                'managed': False,
            },
        ),
    ]
