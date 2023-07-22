from django.urls import path
from .views import PostList, PostDetail

app_name = 'deal'

urlpatterns = [
    path('deal/<int:pk>/', PostDetail.as_view(), name='detailcreate'),
    path('deal', PostList.as_view(), name='listcreate'),
]