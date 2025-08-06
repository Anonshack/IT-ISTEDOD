from django.contrib import admin
from .models import (
    UsefulProgram,
    OnlineResource,
    VideoResource
)
models = [
    UsefulProgram,
    OnlineResource,
    VideoResource
]
for i in models:
    admin.site.register(i)
