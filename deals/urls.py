from django.urls import path
from .views import DealViewSet, DealsByCountryViewSet,DealsByYearViewSet, ValueOfDealsByCountry, quarteryValueOfDeals, ImportDataView, FilterDeals

urlpatterns = [
    path("deal", DealViewSet.as_view({
        'get':'list',
        'post':'create',
    })),
    #  path("deal/<str:pk>", DealViewSet.as_view({
    #     'get':'retrieve',
    #     'put':'update',
    #     'delete':'destroy',
    # })),
       path("dealbyCountry", DealsByCountryViewSet.as_view({
        'get':'list'
        # 'post':'create'
    })),
         path("dealbyYear", DealsByYearViewSet.as_view({
        'get':'list'
        # 'post':'create'
    })),
        path("valueByCountry", ValueOfDealsByCountry.as_view({
        'get':'list'
        # 'post':'create'
    })),
        path("quartlyValue", quarteryValueOfDeals.as_view({
        'get':'list'
        # 'post':'create'
    })),
     path("filter_deals", FilterDeals.as_view({
        'get':'list'
        # 'post':'create'
    })),
        path('import/', ImportDataView.as_view(http_method_names=['post']), name='import_data'),
        # path("import", ImportDataView.as_view({
        # 'post':'import_data'
        # 'post':'create'
    # })),
    
    
]