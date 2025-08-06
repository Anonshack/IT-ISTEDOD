from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (
    DocumentListCreateView, DocumentDetailView,
    AdvertListCreateView, AdvertDetailView,
    CompensationListCreateView, CompensationDetailView,
    RecommendsModelListCreateView, RecommendsModelDetailView,
    SuccessWayListCreateView, SuccessWayDetailView,
    MinistryScholarshipListCreateView, MinistryScholarshipDetailView,
    OrganizationListCreateView, OrganizationDetailView,
    CertificateCategoryListCreateView, CertificateCategoryDetailView,
    CertificateListCreateView, CertificateDetailView,
)

urlpatterns = [
    path('documents/', DocumentListCreateView.as_view(), name='document-list'),
    path('documents/<int:pk>/', DocumentDetailView.as_view(), name='document-detail'),

    path('adverts/', AdvertListCreateView.as_view(), name='advert-list'),
    path('adverts/<int:pk>/', AdvertDetailView.as_view(), name='advert-detail'),

    path('compensations/', CompensationListCreateView.as_view(), name='compensation-list'),
    path('compensations/<int:pk>/', CompensationDetailView.as_view(), name='compensation-detail'),

    path('recommends/', RecommendsModelListCreateView.as_view(), name='recommends-list'),
    path('recommends/<int:pk>/', RecommendsModelDetailView.as_view(), name='recommends-detail'),

    path('success-ways/', SuccessWayListCreateView.as_view(), name='successway-list'),
    path('success-ways/<int:pk>/', SuccessWayDetailView.as_view(), name='successway-detail'),

    path('ministry-scholarships/', MinistryScholarshipListCreateView.as_view(), name='ministry-scholarship-list'),
    path('ministry-scholarships/<int:pk>/', MinistryScholarshipDetailView.as_view(), name='ministry-scholarship-detail'),

    path('organizations/', OrganizationListCreateView.as_view(), name='organization-list'),
    path('organizations/<int:pk>/', OrganizationDetailView.as_view(), name='organization-detail'),

    path('certificate-categories/', CertificateCategoryListCreateView.as_view(), name='certificate-category-list'),
    path('certificate-categories/<int:pk>/', CertificateCategoryDetailView.as_view(), name='certificate-category-detail'),

    path('certificates/', CertificateListCreateView.as_view(), name='certificate-list'),
    path('certificates/<int:pk>/', CertificateDetailView.as_view(), name='certificate-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
