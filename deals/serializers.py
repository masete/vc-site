from rest_framework import serializers
from .models import Deal

class DealsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deal
        fields = ['id','amount', 'company', 'company_slug', 'email', 'funding_round', 'investors', 'valuation_note', 'when']
        # fields = ['when', 'company', 'amount', 'funding_round', 'investors', 'source', 'created_at', 'updated_at', 'user_id', 'company_slug', 'email', 'publish', 'valuation_note', 'year', 'quarter', 'selected_country']


class DealByCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Deal
        fields = ['selected_country', 'deals_count']


class DealByYearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deal
        fields = ['year']