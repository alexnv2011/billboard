from django.urls import path
from .views import PostsList, RepliesList, PostCreate, ReplyCreate, PostDetail, PostEdit, PostDelete, ReplyDelete, accept_me


urlpatterns = [
   path('',                 PostsList.as_view(), name='posts'),
   path('post/<int:pk>',      PostDetail.as_view(),  name='post_detail'),  # cache_page(60*5)(NewsDetail.as_view())),
   path('post/create/',          PostCreate.as_view(),   name='post_create'),
   path('post/<int:pk>/edit/',   PostEdit.as_view(),     name='post_edit'),
   path('post/<int:pk>/delete/', PostDelete.as_view(),   name='post_delete'),
   path('replies/',              RepliesList.as_view(),  name='replies'),
   path('reply/create/',         ReplyCreate.as_view(),   name='reply_create'),
   path('reply/<int:pk>/accept/',  accept_me,   name='accept'),
   path('reply/<int:pk>/delete/', ReplyDelete.as_view(),  name='reply_delete'),

]