from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    # path('', include('car.urls'))
    # path('library/', include('car.urls'))
    path('', include('my_app.urls'))
]
