

# 在你的app的models.py文件中
from django.db import models


class UserProfile(models.Model):
    email = models.TextField(verbose_name="邮箱", default='placeholder@example.com')
    score = models.IntegerField(verbose_name="高考分数")
    rank = models.IntegerField(verbose_name="高考排名")
    subject_choices = (
        ('PC', '物理+化学+不限'),
        ('P', '物理+不限'),
        ('H', '历史+不限'),
    )
    subject = models.CharField(max_length=2, choices=subject_choices, verbose_name="所选科目")
    interest = models.TextField(verbose_name="兴趣(兴趣请输入契合度最高的三个字母)",default='如需获取数据请访问https://yz1.chhniot.cn/pages/evaluation/detail-jmy?id=1751790519583346688&msclkid=1630f747cf9a1db1b61a91c88e6e6f90#,只键入前三个字母')
    res = models.TextField(verbose_name="查询结果")


