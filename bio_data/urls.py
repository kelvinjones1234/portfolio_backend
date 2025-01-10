from django.urls import path
from .views import AllDataView


urlpatterns = [path("all-data/", AllDataView.as_view(), name="all_data")]
