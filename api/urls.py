from django.urls import path
from . import views

urlpatterns = [
    # path('api/', views.UserListCreate.as_view()),
    path('api/', views.UserListCreate.as_view()),

]