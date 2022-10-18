from django.urls import path
from .views import ExcelPageView, ExportExcelfile
urlpatterns = [
    path("", ExcelPageView.as_view()),
    path("download/", ExportExcelfile, name="export"),
]
