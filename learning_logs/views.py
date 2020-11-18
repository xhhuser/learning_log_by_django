from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.http import HttpResponseRedirect  # 用户提交主题后将使用此类将用户重定向到网页topics
from django.urls import \
    reverse  # 根据指定的URL模型创建URL，页面被请求时就会生成URL(django2.0把原来的django.core.urlresolvers包更改为了django.urls包)
from django.contrib.auth.decorators import login_required  # 导入装饰器，对于某些页面只允许已登陆的用户访问

from .models import Topic, Entry  # 导入模型
from .forms import TopicForm, EntryForm  # 导入表单


# 在这里创建视图
def index(request):
    """学习笔记的主页"""
    return render(request, 'learning_logs/index.html')


@login_required  # 先运行装饰器中的代码（检查用户是否已登录）
def topics(request):
    """展示所有的主题"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')  # 根据时间进行排序并都存进topics
    # filter让Django只从数据可中获取owner为对应用户的Topic对象
    context = {'topics': topics}  # 将要发给模板的上下文
    return render(request, 'learning_logs/topics.html', context)


@login_required  # 先运行装饰器中的代码（检查用户是否已登录）
def topic(request, topic_id):
    """显示单个主题及其所有的条目"""
    topic = Topic.objects.get(id=topic_id)
    # 确认请求的主题属于当前用户
    if topic.owner != request.user:
        raise Http404  # 返回404界面
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


@login_required  # 先运行装饰器中的代码（检查用户是否已登录）
def new_topic(request):
    """添加新主题"""
    if request.method != 'POST':
        # 未提交数据；创建一个新表单（空表单）
        form = TopicForm()
    else:
        # POST提交的数据，对数据进行处理
        form = TopicForm(request.POST)  # request.POST是用户输入的内容
        if form.is_valid():  # 自动验证输入内容是否有效
            new_topic = form.save(commit=False)  # 表单内容存入新主题，先不保存进数据库
            new_topic.owner = request.user  # 指定当前用户
            new_topic.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))  # reverse获取topics的URL，并重定向到该网页

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


@login_required  # 先运行装饰器中的代码（检查用户是否已登录）
def new_entry(request, topic_id):
    """为特定主题添加新条目。"""
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404  # 返回404界面
    if request.method != 'POST':
        # 未提交数据；创建空白表单。
        form = EntryForm()
    else:
        # POST提交的数据，对数据进行处理。
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)  # 暂时不存入数据库中
            new_entry.topic = topic
            new_entry.save()  # 设置好了指定主题再保存
            return HttpResponseRedirect(reverse('learning_logs:topic',
                                                args=[topic_id]))  # args参数用来传输当前条目的指定主题ID

    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


@login_required  # 先运行装饰器中的代码（检查用户是否已登录）
def edit_entry(request, entry_id):
    """编辑已有条目"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404  # 返回404界面
    if request.method != 'POST':
        # 初次请求，使用当前条目填充表单
        form = EntryForm(instance=entry)
    else:
        # POST提交数据，对数据进行处理
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',
                                                args=[topic.id]))

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)


def delete_entry(request, entry_id):
    """编辑已有条目"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404  # 返回404界面
    entry.delete()
    return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))  # 删除结束重新指向刷新页面
