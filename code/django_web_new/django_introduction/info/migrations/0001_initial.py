# Generated by Django 4.2 on 2024-07-11 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.TextField(default='placeholder@example.com', verbose_name='邮箱')),
                ('score', models.IntegerField(verbose_name='高考分数')),
                ('rank', models.IntegerField(verbose_name='高考排名')),
                ('subject', models.CharField(choices=[('PC', '物理+化学+不限'), ('P', '物理+不限'), ('H', '历史+不限')], max_length=2, verbose_name='所选科目')),
                ('interest', models.TextField(max_length=3, verbose_name='兴趣(兴趣请输入契合度最高的三个字母)')),
            ],
        ),
    ]
