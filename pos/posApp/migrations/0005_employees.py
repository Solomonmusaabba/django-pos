# Generated by Django 3.2.6 on 2022-11-08 13:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posApp', '0004_salesitems'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=100)),
                ('firstname', models.TextField()),
                ('middlename', models.TextField(blank=True, null=True)),
                ('username', models.TextField()),
                ('password', models.CharField(max_length=100)),
                ('lastname', models.TextField()),
                ('gender', models.TextField(blank=True, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('contact', models.TextField()),
                ('address', models.TextField()),
                ('email', models.TextField()),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
