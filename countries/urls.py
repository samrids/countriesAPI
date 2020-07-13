from django.conf.urls import url
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token  # <-- Here
from countries import views


urlpatterns = [
    path('api/countries/', views.countries_list),
    path('api/countries/<int:pk>', views.countries_detail),    
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # <-- And here
]