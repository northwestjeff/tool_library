"""tool_library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from library import views as library_views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', library_views.home, name='home'),
    url(r'^tools/$', library_views.toolShelf, name='tools'),
    url(r'^tools/(?P<tool_id>[0-9]+)', library_views.viewTool, name='viewtools'),
    url(r'^newtool/$', library_views.newTool, name='newtool'),
    url(r'^edittool/$', library_views.editTools, name='edittools'),
    url(r'^toolupdate/(?P<tool_id>[0-9]+)', library_views.updateTool, name='updatetools'),
    url(r'^users/$', library_views.adminViewUser, name='adminviewuser'),
    url(r'^users/(?P<id>[0-9]+)', library_views.viewUser, name='viewuser'),
    url(r'^newuser/$', library_views.newUserForm, name='newuserform'),
    url(r'^delete/$', library_views.delete, name='delete_tool'),
    url(r'^add/$', library_views.add, name='add_tool'),
    url(r'^update/$', library_views.update, name='update'),
    url(r'^checkout/$', library_views.checkoutTool, name='checkout'),
    url(r'^login/$', auth_views.login, name='login'),
    # url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^log/$', library_views.viewActivityLog, name='logout'),
]


# from django.conf.urls import url
# from django.contrib import admin
# from django.contrib.auth import views as auth_views
#
# urlpatterns = [
#     url(r'^login/$', auth_views.login, name='login'),
#     url(r'^logout/$', auth_views.logout, name='logout'),
#     url(r'^admin/', admin.site.urls),
# ]
