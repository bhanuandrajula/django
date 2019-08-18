
from django.urls import path

from .views import (blog_post_detail_page,
                    blog_post_create_page,
                    blog_post_delete_page,
                    blog_post_list_page,
                    blog_post_update_page)


urlpatterns = [
    path('', blog_post_list_page, name='list_page'),
    path('create/', blog_post_create_page,name='create_page'),
    path('<str:slug>/', blog_post_detail_page,name='detail_page'),
    path('<str:slug>/edit/', blog_post_update_page,name='update_page'),
    path('<str:slug>/delete/', blog_post_delete_page,name='delete_page'),

]
