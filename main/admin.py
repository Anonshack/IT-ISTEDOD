from django.contrib import admin
from .models import (
    Document,
    Advert,
    Compensation,
    RecommendsModel,
    SuccessWay,
    MinistryScholarship,
    Organization,
    CertificateCategory,
    Certificate
)
models = [
    Document,
    Advert,
    Compensation,
    RecommendsModel,
    SuccessWay,
    MinistryScholarship,
    Organization,
    CertificateCategory,
    Certificate,
]

for i in models:
    admin.site.register(i)

# admin.site.register(MinistryScholarship)