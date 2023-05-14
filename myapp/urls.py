from django.urls import path
from myapp import views

urlpatterns = [
     path('student/', views.ContactList.as_view()),
     path('student/<int:pk>/', views.ContactDetail.as_view()),
]