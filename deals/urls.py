from django.urls import path
from django.views.generic import TemplateView
# from .views import PostList, PostDetail

app_name = 'deals'

urlpatterns = [
    path('', TemplateView.as_view(template_name="deals/index.html"), name='index'),
    # path('deal/<int:pk>/', PostDetail.as_view(), name='detailcreate'),
    # path('deal', PostList.as_view(), name='listcreate'),
]