from django.conf.urls import url
from . import views
#Each URL is connected to an HTML response
app_name = 'list'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name = 'index'),

    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name = 'detail'),

    url(r'list/add/$', views.WishListCreate.as_view(), name = 'wishlist-add'),

    url(r'list/(?P<pk>[0-9]+)/delete/$', views.WishListDelete.as_view(), name = 'wishlist-delete'),

    url(r'^(?P<wishlist_id>[0-9]+)/create_book/$', views.create_book, name='create_book'),

    url(r'^(?P<wishlist_id>[0-9]+)/delete_book/(?P<book_id>[0-9]+)/$', views.delete_book, name='delete_book'),

]