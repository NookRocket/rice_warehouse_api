from django.urls import path
from . import views

app_name = "api"

urlpatterns = [
    path("", views.SeedListCreate.as_view(), name="all"),
    path("update/<int:pk>/", views.SeedRetrieveUpdateDestroy.as_view(), name="update"),
    path("add/", views.SeedCreate.as_view(), name="add"),
    path('delete/<int:pk>/', views.SeedDetroy.as_view(), name='delete'),
    path('<int:pk>/', views.SeedRetrieve.as_view(), name="detail")
]
