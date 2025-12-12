
from django.urls import path
from . import views

urlpatterns=[
    path('home/',views.home),
    path('<int:id>/',views.details,name='post'),
    # path('<str:n>/',views.title)
]