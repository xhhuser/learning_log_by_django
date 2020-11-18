from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse  # 根据指定的URL模型创建URL，页面被请求时就会生成URL(django2.0把原来的django.core.urlresolvers包更改为了django.urls包)
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm  # 导入默认注册表单


# 在下面建立自己的视图
def logout_view(request):
    """用户注销视图"""
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))  # 重定向到主页


def register(request):
    """注册新用户"""
    if request.method != 'POST':
        # 显示空的注册表单
        form = UserCreationForm()
    else:
        # 处理填写好的表单
        form = UserCreationForm(data=request.POST)

        if form.is_valid():  # 检查是否有效，是否有非法字符，密码是否相同等
            new_user = form.save()
            # 让用户自动登录，再重定向到主页
            authenticated_user = authenticate(username=new_user.username,
                                              password=request.POST['password1'])
            # 用鉴定函数检验用户密码，返回一个通过验证的用户对象
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))

    context = {'form': form}
    return render(request, 'users/register.html', context)
