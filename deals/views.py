from rest_framework import viewsets
from rest_framework import pagination
from django.views import View
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from django.db.models import Count, Sum, Q, F
from .models import Deal
from rest_framework import serializers
from .serializers import DealsSerializer, DealByCountrySerializer, DealByYearSerializer
from django.conf import settings
import math
import os
import pandas as pd
from django.http import HttpResponse
from django.db.models import F


class CustomPagination(pagination.PageNumberPagination):
    page_size = 10


class ImportDataView(View):
    def import_data(self, request):
        # Read the uploaded file
        # file = os.path.join(settings.BASE_DIR, '/home/nicholas/Documents/data science/merchant/deals/cleane_data.xlsx')
        file = os.path.join(settings.BASE_DIR, 'cleane_data.xlsx')
        # file = request.FILES['file']  # Assuming you have a file upload field named 'file'
        df = pd.read_excel(file)

        # Remove duplicates
        df = df.drop_duplicates()

        # Save the cleaned data to the database
        # Replace 'YourModel' with your actual Django model
        Deal.objects.bulk_create(
            Deal(**row) for row in df.to_dict(orient='records')
        )

        return HttpResponse('Data imported successfully.')


class DealViewSet(viewsets.ViewSet):
    def list(self, request):

        # page = int(request.GET.get('page', 1))
        # per_page = 9
           # Define the fields you want to exclude
        excluded_fields = ['user_id', 'updated_at', 'source', 'publish', 'created_at']
        deals = Deal.objects.all().exclude(**{field: F(field) for field in excluded_fields})


        paginator = CustomPagination()
        result_page = paginator.paginate_queryset(deals, request)

         # Serialize the paginated queryset
        serializer = DealsSerializer(result_page, many=True)

        # Return the paginated response
        return paginator.get_paginated_response(serializer.data)

        # total = deals.
        # start = (page - 1) * per_page
        # end = page * per_page
        # serializer = DealsSerializer(deals, many=True)
        # serializer = DealSerializer(deals[start:end], many=True)
        # return Response({
        #     'data': serializer.data,
        #     'total':total,
        #     'page': page,
        #     'last_page': math.ceil(total/per_page)

        #     })
        # return Response(serializer.data)

    def create(self, request):
        serializer = DealsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        deals = Deal.objects.get(id=pk)
        serializer = DealsSerializer(deals)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        deals = Deal.objects.get(id=pk)
        serializer = DealsSerializer(instance=deals, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        pass

class FilterDeals(viewsets.ViewSet):
    def list(self, request):
        funding_round = request.GET.get('funding_round')
        # sector = request.GET.get('sector')
        limit = int(request.GET.get('limit', 10))  # Default limit is set to 10

        # Filter the deals based on funding_type and sector
        deals = Deal.objects.filter(funding_round=funding_round)[:limit]

         # Serialize the filtered deals
        serializer = DealsSerializer(deals, many=True)

        return Response(serializer.data)

class DealsByCountryViewSet(viewsets.ViewSet):
    def list(self, request):
        # Fetch deals count by country from the 'investment' table
        deals_count_by_country = Deal.objects.values('selected_country').annotate(deals_count=Count('id'))

          # Filter out records with empty strings and null values for selected_country
        deals_count_by_country = deals_count_by_country.exclude(Q(selected_country='') | Q(selected_country__isnull=True))

        # Serialize the data for plotting
        serialized_data = [{'selected_country': deal['selected_country'], 'deals_count': deal['deals_count']} for deal in deals_count_by_country]

        serializer = DealByCountrySerializer(deals_count_by_country, many=True)

        return Response({'data': serialized_data})


class DealsByYearViewSet(viewsets.ViewSet):
    def list(self, request):
        deals = Deal.objects.exclude(year=None).values('year').annotate(count=Count('id'))
        return JsonResponse(list(deals), safe=False)
        # serializer = DealByYearSerializer(deals, many=True) 
        # return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    
class ValueOfDealsByCountry(viewsets.ViewSet):
    def list(self, request):
        # data = Deal.objects.values('selected_country').annotate(total_amount=Sum('amount'))
        data = Deal.objects.values('selected_country').annotate(total_amount=Sum('amount')).order_by('-total_amount')[:15]
        return JsonResponse(list(data), safe=False)

class quarteryValueOfDeals(viewsets.ViewSet):    
    def list(self, request):
        data = Deal.objects.values('quarter').annotate(total_amount=Sum('amount'))
        return JsonResponse(list(data), safe=False)
 
#  class DealsList