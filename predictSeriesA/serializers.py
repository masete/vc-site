from rest_framework import serializers
# from .models import PredictSeriesA

class PredictSeriesASerializer(serializers.ModelSerializer):
    class Meta:
        # model = PredictSeriesA
        fields = ['id','Last_funding_round_raised_amount','age_of_company','Amount_of_the_last_funding_type',
                  'Companies_Information_Level_of_Completeness','Stage_DA_Classified_Early','number_of_founders',
                  'number_of_bussiness_categories','number_of_market_countires','Female_Co_Founder',
                  'Average_time_of_rounds','number_of_investors','Sector_Information_Technology','Business_model_B2C']