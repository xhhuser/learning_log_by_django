from django.contrib import admin
from django.conf.urls import include, url

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^users/', include(('users.urls', "users"), namespace='users')),      #将自己的程序URL包含到总的urls中来
    url(r'', include(('learning_logs.urls', "learning_logs"), namespace='learning_logs')),   #这里include要用二元元祖
]
