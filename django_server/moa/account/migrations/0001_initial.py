# Generated by Django 3.1.7 on 2021-06-02 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('user_id', models.CharField(max_length=64, primary_key=True, serialize=False, unique=True)),
                ('password', models.CharField(max_length=64)),
                ('name', models.CharField(max_length=64)),
                ('phone', models.CharField(max_length=64, unique=True)),
                ('email', models.CharField(max_length=64, unique=True)),
                ('birth', models.CharField(max_length=64)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Customer',
                'verbose_name_plural': 'Customer',
                'db_table': 'customer',
            },
        ),
    ]
