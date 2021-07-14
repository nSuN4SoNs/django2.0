from django.urls import path, include
from car.views import CarListView, CarDetailView, CarCreateView
urlpatterns = [
    path("car/", CarListView.as_view(), name="car-list" ),
    path("car/create", CarCreateView.as_view(), name="car-create" ),
    path("car/<int:pk>", CarDetailView.as_view(), name="car-detail" ),
]

from car.views import CarModelListView, CarModelDetailView, CarModelCreateView
urlpatterns = [
    path("carmodel/", CarModelListView.as_view(), name="carmodel-list" ),
    path("carmodel/create", CarModelCreateView.as_view(), name="carmodel-create" ),
    path("carmodel/<int:pk>", CarModelDetailView.as_view(), name="carmodel-detail" ),
]

from car.views import CompanyListView, CompanyDetailView, CompanyCreateView
urlpatterns = [
    path("carcompany/", CompanyListView.as_view(), name="carcompany-list" ),
    path("carcompany/create", CompanyCreateView.as_view(), name="carcompany-create" ),
    path("carcompany/<int:pk>", CompanyDetailView.as_view(), name="carcompany-detail" ),
]