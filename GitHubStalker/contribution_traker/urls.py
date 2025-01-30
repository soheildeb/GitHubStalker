from django.urls import path
from .views import get_contributions_data, index

urlpatterns = [
    path("", index, name="index"),
    path("contributions/<username>/", get_contributions_data, name="get_contributions_data"),
]
