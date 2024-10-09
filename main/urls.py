from django.urls import re_path as url

from main import views

urlpatterns = [
    url(r'^books/$', views.get_books, name="books"),
    url(r'^create_book/$', views.create_book, name="create_book"),
    url(r'^delete_book/$', views.delete_book, name="delete_book"), 
    url(r'^book_by_id/$', views.book_by_id, name="book_by_id"),
    url(r'^filter_book/$', views.filter_book, name="filter_book"),
    url(r'^create_user', views.create_user, name="create_user"),
    url(r'^get_all_users', views.get_all_users, name="get_all_users"),
    url(r'^user_details/$', views.user_details, name="user_details"),
    url(r'^update_user/$', views.update_user, name="update_user"),
    url(r'^delete_user/$', views.delete_user, name="delete_user"),
    url(r'^update_book/$', views.update_book, name="update_book"),
]