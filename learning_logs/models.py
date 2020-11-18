from django.db import models
from django.contrib.auth.models import User  # 导入已有的User模型


# 在此处创建模型。
class Topic(models.Model):
    """用户正在学习的主题。"""
    text = models.CharField(max_length=200)  # charfield可以存储少量的文本
    date_added = models.DateTimeField(auto_now_add=True)  # datatimefield是记录时间和日期的数据，这里每次新建自动传递实参
    owner = models.ForeignKey(User, on_delete=models.CASCADE)  # 添加字段owner，建立与模型User的外键关系

    def __str__(self):
        """返回模型的字符串表示，将用户主题用文字显示出来。"""
        return self.text


class Entry(models.Model):
    """关于某一主题的特定知识（条目）。"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)  # ForeignKey建立一个外键,django2.0之后外键需要加上on_delete
    text = models.TextField()  # textfield不限制文本的长度
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:  # 特殊情况另命名，不用的话会变成entrys
        verbose_name_plural = 'entries'

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text[:50] + "..."
