from django.conf.urls import url
from django.urls import path, re_path
from  .views import item_page, edit_page, hello, delete_page, search_page,stream_http_download
app_name="item"
urlpatterns = [
     url(r'^(?P<id>[\w-]+)/$',item_page , name='item_page'),
     url(r'^edit/(?P<id>[\w-]+)/$',edit_page , name='edit_page'),
      url(r'^delete/(?P<id>[\w-]+)/$', delete_page , name='delete_page'),
      url(r'^search/search$', search_page , name='search_page'),
     url(r'^hello/hello/$',hello,name="hello"),
     re_path(r'^download/download/(?P<file_path>.*)/$', stream_http_download, name='file_download'),
]