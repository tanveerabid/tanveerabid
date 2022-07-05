# Generated by Django 4.0.3 on 2022-07-04 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('download', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('business', models.CharField(max_length=50)),
                ('ntn', models.CharField(max_length=50)),
                ('discription', models.TextField(max_length=100)),
                ('public_status', models.BooleanField(default=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Invoive',
                'verbose_name_plural': 'Invoices',
            },
        ),
    ]
