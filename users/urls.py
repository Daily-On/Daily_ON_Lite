from django.urls import path
from users import apis, views

app_name = "users"

urlpatterns =[
    path('rest-auth/kakao/', views.KakaoLogin.as_view(), name='kakao'),
    path('rest-auth/naver/', views.NaverLogin.as_view(), name='naver'),
    path('rest-auth/google/', views.GoogleLogin.as_view(), name='google'),

 ]