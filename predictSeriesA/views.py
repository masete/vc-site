from django.http import JsonResponse
from .models import PredictSeriesA
from .serializers import PredictSeriesASerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

import pickle
import numpy as np

with open("model.pkl", "rb") as f:
    model = pickle.load(f)


@api_view(['POST'])
def predict_series_A(request):
    try:
        form_values = request.data
        column_names = [
            "Last_funding_round_raised_amount",
            "age_of_company",
            "Amount_of_the_last_funding_type",
            "Companies_Information_Level_of_Completeness",
            "Stage_DA_Classified_Early",
            "number_of_founders",
            "number_of_bussiness_categories",
            "number_of_market_countires",
            "Female_Co_Founder",
            "Average_time_of_rounds",
            "number_of_investors",
            "Sector_Information_Technology",
            "Business_model_B2C"
        ]

        input_data = np.asarray([float(form_values[i]) for i in column_names]).reshape(1, -1)
        # prediction = model.predict_proba(input_data)
        prediction = model.predict_proba(input_data)

        # types = {
        #     0: "According to our data and the metrics provided, there are Low chances of the startup being successful",
        #     1: "According to our data and the metrics provided, there are High chances that the startup will be successful"
        # }

        response_data = {
            "statusCode": 200,
            "status": "Prediction made",
            "result": "There are: " + str(prediction[0] * 100)
            # "result": "There are: " + types[prediction[0]] *100
            # (f"There is a {probability * 100:.2f}% chance that this startup will make it to Series A.")
        }

        return JsonResponse(response_data, safe=False)
    except Exception as e:
        return JsonResponse({"error": "Please Enter Valid Data"}, status=400)
    

@api_view(['GET', 'POST'])
def predictSeriesA(request, format=None):

    if request.method == 'GET':
        predictions = PredictSeriesA.objects.all()
        serializer = PredictSeriesASerializer(predictions, many=True)
        return JsonResponse(serializer.data, safe=False)
    

    if request.method == 'POST':
        serializer = PredictSeriesASerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        

@api_view(['GET', 'PUT', 'DELETE'])
def predictSeriesA_detail(request, id, format=None):

    try:
        pred = PredictSeriesA.objects.get(pk=id)
    except PredictSeriesA.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serilizer = PredictSeriesASerializer(pred)
        return Response(serilizer.data)
    if request.method == 'PUT':
        serializer = PredictSeriesASerializer(pred, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        pred.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)