"""blog3 URL Configuration

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
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from blog.views import HomePageView, PostList, DetailPost, AddPost, EditPost, DeletePost, RegisterFormView, LoginFormView, LogoutView, AddComment

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^post_list/$', PostList.as_view(), name='post_list'),
    url(r'^posts/(?P<pk>[0-9]+)$', DetailPost.as_view(), name='detail_post'),
    url(r'^posts/add/$', AddPost.as_view(), name='create_post'),
    url(r'^posts/edit/(?P<pk>[0-9]+)$', EditPost.as_view(), name='edit_post'),
    url(r'^posts/delete/(?P<pk>[0-9]+)$', DeletePost.as_view(), name='delete_post' ),
    url(r'^register/$', RegisterFormView.as_view(), name='register'),
    url(r'^login/$', LoginFormView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^posts/add_comment/$', AddComment.as_view(), name='add_comment'),
    url(r'^current_author_posts/$', PostList.as_view(), name='author_posts'),
]
