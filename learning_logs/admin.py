from django.contrib import admin
from learning_logs.models import Topic, Entry   #自己创建的模型必须手动注册
# 在这里注册你的模型

admin.site.register(Topic)      #可通过管理网站来管理自己的模型
admin.site.register(Entry)
