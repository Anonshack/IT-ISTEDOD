from django.contrib import admin
from .models import (
    MajorCategory,
    Level,
    ListDocument,
    Company,
    Table
)
models = [MajorCategory, Level, ListDocument, Company, Table]
for i in models:
    admin.site.register(i)