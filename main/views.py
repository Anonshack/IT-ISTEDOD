from rest_framework import generics
from table_part.permissions import IsAdminOrReadOnly
from .models import (
    Document, Advert, Compensation, RecommendsModel, SuccessWay,
    MinistryScholarship, Organization, CertificateCategory, Certificate
)
from .serializers import (
    DocumentSerializer, AdvertSerializer, CompensationSerializer, RecommendsModelSerializer,
    SuccessWaySerializer, MinistryScholarshipSerializer, OrganizationSerializer,
    CertificateCategorySerializer, CertificateSerializer
)

# Document views
class DocumentListCreateView(generics.ListCreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [IsAdminOrReadOnly]

class DocumentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [IsAdminOrReadOnly]

# Advert views
class AdvertListCreateView(generics.ListCreateAPIView):
    queryset = Advert.objects.all()
    serializer_class = AdvertSerializer
    permission_classes = [IsAdminOrReadOnly]

class AdvertDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Advert.objects.all()
    serializer_class = AdvertSerializer
    permission_classes = [IsAdminOrReadOnly]

# Compensation views
class CompensationListCreateView(generics.ListCreateAPIView):
    queryset = Compensation.objects.all()
    serializer_class = CompensationSerializer
    permission_classes = [IsAdminOrReadOnly]

class CompensationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Compensation.objects.all()
    serializer_class = CompensationSerializer
    permission_classes = [IsAdminOrReadOnly]

# RecommendsModel views
class RecommendsModelListCreateView(generics.ListCreateAPIView):
    queryset = RecommendsModel.objects.all()
    serializer_class = RecommendsModelSerializer
    permission_classes = [IsAdminOrReadOnly]

class RecommendsModelDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RecommendsModel.objects.all()
    serializer_class = RecommendsModelSerializer
    permission_classes = [IsAdminOrReadOnly]

# SuccessWay views
class SuccessWayListCreateView(generics.ListCreateAPIView):
    queryset = SuccessWay.objects.all()
    serializer_class = SuccessWaySerializer
    permission_classes = [IsAdminOrReadOnly]

class SuccessWayDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SuccessWay.objects.all()
    serializer_class = SuccessWaySerializer
    permission_classes = [IsAdminOrReadOnly]

# MinistryScholarship views
class MinistryScholarshipListCreateView(generics.ListCreateAPIView):
    queryset = MinistryScholarship.objects.all()
    serializer_class = MinistryScholarshipSerializer
    permission_classes = [IsAdminOrReadOnly]

class MinistryScholarshipDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MinistryScholarship.objects.all()
    serializer_class = MinistryScholarshipSerializer
    permission_classes = [IsAdminOrReadOnly]

# Organization views
class OrganizationListCreateView(generics.ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [IsAdminOrReadOnly]

class OrganizationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [IsAdminOrReadOnly]

# CertificateCategory views
class CertificateCategoryListCreateView(generics.ListCreateAPIView):
    queryset = CertificateCategory.objects.all()
    serializer_class = CertificateCategorySerializer
    permission_classes = [IsAdminOrReadOnly]

class CertificateCategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CertificateCategory.objects.all()
    serializer_class = CertificateCategorySerializer
    permission_classes = [IsAdminOrReadOnly]

# Certificate views
class CertificateListCreateView(generics.ListCreateAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    permission_classes = [IsAdminOrReadOnly]

class CertificateDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    permission_classes = [IsAdminOrReadOnly]
