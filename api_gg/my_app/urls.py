from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('index1/<int:pk>', views.Post_update_and_detail)
]
