

# 在你的app的models.py文件中
from django.db import models


class UserProfile(models.Model):
    email = models.EmailField(default="")
    score = models.IntegerField(default="")
    rank = models.IntegerField(default="")
    subject_choices = (
        ('PC', '物理+化学+不限'),
        ('P', '物理+不限'),
        ('H', '历史+不限'),
    )
    subject = models.CharField(max_length=2, choices=subject_choices, verbose_name="所选科目",default="")
    interest = models.CharField(max_length=3,verbose_name="兴趣(兴趣请输入契合度最高的三个字母)",default="")
    finalinfo=models.CharField(default="",max_length=1000)

