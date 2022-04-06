from django.contrib import admin
from django.urls import path, include
from financepy.views import RegisterViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'register', RegisterViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
