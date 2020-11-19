from django.urls import path
from API.views import *



app_name = 'api'


urlpatterns =[
    path('product', ProductAdd.as_view()),
    path('product/<pk>', ProductView.as_view()),
]
