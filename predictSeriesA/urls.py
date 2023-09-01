from django.contrib import admin
from django.urls import path
from predictSeriesA import views
# from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # path("predictSeriesA/", views.predictSeriesA),
    path("predictSeriesA/",views.predict_series_A, name='predict_series_A')
]