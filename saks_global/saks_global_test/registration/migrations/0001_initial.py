# Generated by Django 3.0.2 on 2020-02-27 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('username', models.CharField(blank=True, max_length=255, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('present_address', models.CharField(blank=True, max_length=350, null=True)),
                ('permanent_address', models.CharField(blank=True, max_length=350, null=True)),
                ('nid_number', models.CharField(blank=True, max_length=12, null=True)),
            ],
            options={
                'db_table': 'registration',
            },
        ),
    ]