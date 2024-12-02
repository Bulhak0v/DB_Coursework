# Generated by Django 5.1.3 on 2024-12-02 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carsharing', '0005_promo_code_rental_agreement'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientScore',
            fields=[
                ('client_score_id', models.AutoField(primary_key=True, serialize=False)),
                ('score', models.PositiveSmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], help_text='Score between 1 and 5', verbose_name='Score')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Comment')),
                ('score_date', models.DateField(verbose_name='Score Date')),
            ],
            options={
                'db_table': 'client_score',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('insurance_id', models.AutoField(primary_key=True, serialize=False)),
                ('insurance_type', models.CharField(max_length=100, verbose_name='Insurance Type')),
                ('insurance_value', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Insurance Value')),
                ('insurance_details', models.TextField(blank=True, null=True, verbose_name='Insurance Details')),
            ],
            options={
                'db_table': 'insurance',
                'managed': False,
            },
        ),
    ]
