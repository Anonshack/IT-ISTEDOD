from rest_framework import serializers
from .models import (
    MajorCategory,
    Level,
    ListDocument,
    Company,
    Table
)

class MajorCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = MajorCategory
        fields = '__all__'

class LevelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'

class ListDocumentSerializers(serializers.ModelSerializer):
    class Meta:
        model = ListDocument
        fields = '__all__'


class CompanySerializers(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class TableSerializers(serializers.ModelSerializer):
    major = MajorCategorySerializers()
    level = LevelSerializers()
    company = CompanySerializers()

    class Meta:
        model = Table
        fields = '__all__'
