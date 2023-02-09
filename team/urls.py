from gettext import bindtextdomain

from django.urls import path

from . import views

app_name = 'team'
urlpatterns = [
    path('', views.index, name='index'),
    path('add_member', views.add_member, name='add_member'),
    path('member/<int:pk>', views.edit_member, name='edit_member'),
    path('member/<int:pk>/delete', views.delete_member, name='delete_member'),
]
 