from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser
from .models import MajorCategory, Level, ListDocument, Company, Table
from .serializers import (
    MajorCategorySerializers, LevelSerializers,
    ListDocumentSerializers, CompanySerializers, TableSerializers
)

class CustomPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 50

# 1. Major Category API
class MajorCategoryListView(generics.ListAPIView):
    queryset = MajorCategory.objects.all()
    serializer_class = MajorCategorySerializers
    pagination_class = CustomPagination

class MajorCategoryAdminView(generics.CreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = MajorCategory.objects.all()
    serializer_class = MajorCategorySerializers
    permission_classes = [IsAdminUser]

# 2. Level API
class LevelListView(generics.ListAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializers
    pagination_class = CustomPagination

class LevelAdminView(generics.CreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializers
    permission_classes = [IsAdminUser]

# 3. List Document API
class ListDocumentListView(generics.ListAPIView):
    queryset = ListDocument.objects.all()
    serializer_class = ListDocumentSerializers
    pagination_class = CustomPagination

class ListDocumentAdminView(generics.CreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = ListDocument.objects.all()
    serializer_class = ListDocumentSerializers
    permission_classes = [IsAdminUser]

# 4. Company API
class CompanyListView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializers
    pagination_class = CustomPagination

class CompanyAdminView(generics.CreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializers
    permission_classes = [IsAdminUser]

# 5. Table API
class TableListView(generics.ListAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializers
    pagination_class = CustomPagination

class TableAdminView(generics.CreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializers
    permission_classes = [IsAdminUser]
