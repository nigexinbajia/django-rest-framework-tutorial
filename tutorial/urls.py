"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from quickstart import views as QuickstartViews

router = routers.DefaultRouter()
router.register(r'users', QuickstartViews.UserViewSet)
router.register(r'groups', QuickstartViews.GroupViewSet)

"""
1. 使用URL路由来管理我们的API
2. 另外添加登录相关的URL
"""

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^quickstart/', include(router.urls)),
    url(r'^snippets/', include('snippets.urls')),
    url(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
