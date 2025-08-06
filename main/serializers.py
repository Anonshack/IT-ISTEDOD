from rest_framework import serializers
from .models import (
    Document, Advert, Compensation, RecommendsModel, SuccessWay,
    MinistryScholarship, Organization, CertificateCategory, Certificate
)

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'


class AdvertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advert
        fields = '__all__'


class CompensationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compensation
        fields = '__all__'


class RecommendsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecommendsModel
        fields = '__all__'


class SuccessWaySerializer(serializers.ModelSerializer):
    class Meta:
        model = SuccessWay
        fields = '__all__'


class MinistryScholarshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = MinistryScholarship
        fields = '__all__'


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'


class CertificateCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CertificateCategory
        fields = '__all__'


class CertificateSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    organization_name = serializers.CharField(source='organization.name', read_only=True)

    class Meta:
        model = Certificate
        fields = ['id', 'name', 'category', 'category_name', 'organization', 'organization_name']
