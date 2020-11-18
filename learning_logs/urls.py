"""定义learning_logs的url模式。"""

from django.conf.urls import url

from . import views     # 导入视图

urlpatterns = [
    # 主页
    url(r'^$', views.index, name='index'),     # 此url的名称为index，在其他地方可以直接引用
    # 显示所有的主题
    url(r'^topics/$', views.topics, name='topics'),
    # 单个主题的所有详细信息页面
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    # 用于添加新主题的页面
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
    # 用于添加新条目的页面
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    # 用于编辑条目的页面
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
    # 用于删除条目的页面
    url(r'^delete_entry/(?P<entry_id>\d+)/$', views.delete_entry, name='delete_entry'),  # 将URL指向视图函数delete_entry
]
