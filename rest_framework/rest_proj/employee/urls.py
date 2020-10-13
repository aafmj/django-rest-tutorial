from django.urls import path
from employee import views


urlpatterns = [
    path('post-employee/', views.post_employee),
    path('get-employees/', views.get_employees),
    path('get-update-delete-employee/<int:pk>', views.get_update_delete_employee),
    path('search-employee', views.search_employee)
]