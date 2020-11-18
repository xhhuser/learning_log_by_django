from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):         # 此类继承自forms.ModelForm
    class Meta:
        model = Topic            # 按照指定模型创建表单
        fields = ['text']        # 此表单的字段只有text
        labels = {'text': ''}    # 不为text生成标签(空标签)

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}      # 表单元素，可设置单行文本框、多行文本区域和下拉列表
