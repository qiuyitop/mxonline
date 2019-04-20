# _*_ encoding:utf-8 _*_
"""MxOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
import xadmin

from django.urls import path,include,re_path

from django.views.generic import TemplateView
from users.views import LoginView,RegisterView,ActiveUserView,ForgetPwdView,ResetView,ModifyPwdView
from organization.views import OrgView
from django.views.static import serve
from MxOnline.settings import MEDIA_ROOT
from users.views import LogoutView,IndexView
#from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import staticfiles

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('', IndexView.as_view(),name='index'),
    path('login/',LoginView.as_view(),name = 'login'),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('register/',RegisterView.as_view(),name = 'register'),
    path('captcha/',include('captcha.urls')),
    re_path('active/(?P<active_code>.*)/',ActiveUserView.as_view(),name='user_active'),
    path('forget/',ForgetPwdView.as_view(),name='forget_pwd'),
    re_path('reset/(?P<active_code>.*)/', ResetView.as_view(), name='reset_pwd'),
    path('modify_pwd/', ModifyPwdView.as_view(), name='modify_pwd'),
    # 处理图片显示的url,使用Django自带serve,传入参数告诉它去哪个路径找，我们有配置好的路径MEDIAROOT
    re_path(r'^media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT }),
    path("org/", include('organization.urls', namespace="org")),
    path("course/", include('course.urls', namespace="course")),
    path("users/", include('users.urls', namespace="users")),
    #re_path(r'^static/(?P<path>.*)', serve, {"document_root": STATICFILES_DIRS }),
    path('ueditor/',include('DjangoUeditor.urls' )),
]
urlpatterns += staticfiles_urlpatterns()