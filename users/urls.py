""""定义程序users的url模式。"""

from django.conf.urls import url
from django.contrib.auth.views import LoginView  # 导入Django的登录视图类

from . import views  # 导入视图

urlpatterns = [
    # 登录主页
    url(r'^login/$', LoginView.as_view(template_name='users/login.html'), name='login'),
    # 这里会将URL的login请求发送给默认视图login，因为不是自己编写，需要指定视图模板的位置
    # 从django-1.11开始,基于函数的登录,注销等视图已被重写为基于类的视图:【接下】
    # LoginView 和 LogoutView类,如 release notes中所指定的那样,仍然可以使用“旧的”基于函数的视图,【接下】
    # 但是被标记为已弃用,在django-2.1中,已删除旧的基于功能的视图,如release notes中所述

    # 登出界面
    url(r'^logout/$', views.logout_view, name='logout'),  # 将URL指向视图函数logout_view

    # 注册界面
    url(r'^register/$', views.register, name='register'),
]
