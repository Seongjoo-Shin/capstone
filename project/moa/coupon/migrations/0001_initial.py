# Generated by Django 3.1.7 on 2021-06-02 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_cnt', models.PositiveIntegerField(default='0', verbose_name='현재 개수')),
                ('customer', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to='account.customer', verbose_name='유저 이름')),
                ('store', models.ForeignKey(db_column='cafe_name', on_delete=django.db.models.deletion.CASCADE, to='management.manager', verbose_name='카페 이름')),
            ],
            options={
                'verbose_name': 'coupon',
                'verbose_name_plural': 'coupon',
                'db_table': 'coupon',
            },
        ),
    ]