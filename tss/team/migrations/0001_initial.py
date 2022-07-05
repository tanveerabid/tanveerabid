# Generated by Django 4.0.3 on 2022-04-18 05:19

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields
import team.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('designation', models.CharField(choices=[('', '----------'), ('DIR', 'Director'), ('SEC', 'Secretary'), ('CEO', 'Chief Executive Officer'), ('COO', 'Chief Operating Officer'), ('CSO', 'Chief Security Officer'), ('CMO', 'Chief Marketing Officer'), ('SO', 'Security Officer'), ('SS', 'Security Supervisor')], default='', max_length=3, null=True)),
                ('cnic', models.PositiveBigIntegerField(help_text='CNIC Number')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('emp_status', models.BooleanField(default=True)),
                ('office', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contact.office')),
            ],
            options={
                'verbose_name': 'employee',
                'verbose_name_plural': 'employees',
            },
        ),
        migrations.CreateModel(
            name='employee_profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(max_length=150, verbose_name='Address')),
                ('img', models.ImageField(upload_to=team.models.upload_directory_path, verbose_name='Profile Pic')),
                ('cell_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True, verbose_name='Cell Number')),
                ('fb', models.URLField(blank=True, null=True, verbose_name='Facebook Profile Link')),
                ('twitt', models.URLField(blank=True, null=True, verbose_name='Twitter Profile Link')),
                ('linkedin', models.URLField(blank=True, null=True, verbose_name='Linkedin Profile Link')),
                ('insta', models.URLField(blank=True, null=True, verbose_name='Instagram Profile Link')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('cnic', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='team.employee', verbose_name='Employee Name')),
            ],
            options={
                'verbose_name': 'profile',
                'verbose_name_plural': 'profiles',
            },
        ),
    ]
