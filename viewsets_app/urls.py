from django.urls import path,include
from rest_framework.routers import DefaultRouter
from viewsets_app import views


router = DefaultRouter()
router.register('employees',views.employeeViewSet,basename='employee')

urlpatterns = [
    path('',include(router.urls))
]