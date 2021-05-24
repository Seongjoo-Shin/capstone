# Generated by Django 3.1.7 on 2021-05-23 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fuser', '0004_fuser_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fuser',
            name='password',
            field=models.CharField(max_length=10, verbose_name='비밀번호'),
        ),
        migrations.AlterField(
            model_name='fuser',
            name='user_email',
            field=models.CharField(max_length=10, verbose_name='이메일'),
        ),
        migrations.AlterField(
            model_name='fuser',
            name='user_id',
            field=models.CharField(max_length=10, verbose_name='아이디'),
        ),
        migrations.AlterField(
            model_name='fuser',
            name='user_name',
            field=models.CharField(max_length=10, verbose_name='카페이름'),
        ),
    ]