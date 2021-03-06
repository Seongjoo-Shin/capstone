# Generated by Django 3.1.7 on 2021-06-02 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('cafe_name', models.CharField(max_length=64, primary_key=True, serialize=False, verbose_name='카페')),
                ('cafe_stamp', models.IntegerField(verbose_name='쿠폰개수')),
                ('cafe_explain', models.CharField(max_length=400, verbose_name='카페소개')),
                ('latitude', models.FloatField(verbose_name='위도')),
                ('longtitude', models.FloatField(verbose_name='경도')),
                ('phone', models.CharField(max_length=64, verbose_name='전화번호')),
            ],
            options={
                'verbose_name': '등록 카페',
                'verbose_name_plural': '등록 카페',
                'db_table': 'management',
            },
        ),
    ]
