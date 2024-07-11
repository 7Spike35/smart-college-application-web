from django import forms

# 在你的app的forms.py文件中
from django import forms
from .models import UserProfile  # 导入你的模型


class RecommendationForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['email', 'score', 'rank', 'subject', 'interest', 'res']
