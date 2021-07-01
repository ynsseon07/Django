from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('categoryCreate/', views.categoryCreate, name='cateCreatePage'),
    path('categoryCreate/create', views.Create_category, name='cateCreate'),
    path('restaurantCreate/', views.restaurantCreat, name='resCreatePage'),
    path('restaurantDetail/delete', views.Delete_restaurant, name='resDelete'),
    path('restaurantCreate/create', views.Create_restaurant, name='resCreate'),
    path('restaurantDetail/<str:res_id>', views.restaurantDetail, name='resDetailPage'),
    path('restaurantDetail/updatePage/update', views.Update_restaurant, name='resUpdate'),
    path('restaurantDetail/updatePage/<str:res_id>', views.restaurantUpdate, name='resUpdatePage'),
]