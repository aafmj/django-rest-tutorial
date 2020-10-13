from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('person', views.PersonViewSet)
router.register('car', views.CarViewSet)

urlpatterns = [
    # path('get-post-person', views.person_view),
    # path('get-post-car', views.car_view),
    # path('information', views.information_view)
]

urlpatterns += router.urls
