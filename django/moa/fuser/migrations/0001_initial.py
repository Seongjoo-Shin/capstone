# Generated by Django 3.1.7 on 2021-05-09 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fuser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=64, verbose_name='아이디')),
                ('password', models.CharField(max_length=64, verbose_name='비밀번호')),
                ('register_date', models.DateField(auto_now_add=True, verbose_name='가입날짜')),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]