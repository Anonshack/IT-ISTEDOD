from django.urls import path
from .views import (
    MajorCategoryListView,
    MajorCategoryAdminView,
    LevelListView,
    LevelAdminView,
    ListDocumentListView,
    ListDocumentAdminView,
    CompanyListView,
    CompanyAdminView,
    TableListView,
    TableAdminView
)

urlpatterns = [
    # Major Category part
    path('major-categories/', MajorCategoryListView.as_view(), name='major-category-list'),
    path('major-categories/<int:pk>/', MajorCategoryAdminView.as_view(), name='major-category-detail'),

    # Level part
    path('levels/', LevelListView.as_view(), name='level-list'),
    path('levels/<int:pk>/', LevelAdminView.as_view(), name='level-detail'),

    # Document part
    path('documents/', ListDocumentListView.as_view(), name='documents-list'),
    path('documents/<int:pk>/', ListDocumentAdminView.as_view(), name='document-detail'),

    # Company part
    path('companies/', CompanyListView.as_view(), name='companies-list'),
    path('companies/<int:pk>/', CompanyAdminView.as_view(), name='company-detail'),

    # Table part
    path('tables/', TableListView.as_view(), name='tables-list'),
    path('tables/<int:pk>/', TableAdminView.as_view(), name='table-detail'),
]
