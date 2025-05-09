from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.kakao.views import KakaoOAuth2Adapter
from allauth.socialaccount.providers.naver.views import NaverOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.serializers import SocialLoginSerializer
from dj_rest_auth.registration.views import SocialLoginView
from django.shortcuts import render

# Create your views here.
# 소셜 로그인
BASE_URL =
GOOGLE_CALLBACK_URI = BASE_URL + 'google/callback/'
KAKAO_CALLBACK_URI = BASE_URL + 'kakao/callback/'
NAVER_CALLBACK_URI = BASE_URL + 'naver/callback/'

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = GOOGLE_CALLBACK_URI
    client_class = OAuth2Client
    serializer_class = SocialLoginSerializer

class KakaoLogin(SocialLoginView):
    adapter_class = KakaoOAuth2Adapter
    callback_url = KAKAO_CALLBACK_URI
    client_class = OAuth2Client
    serializer_class = SocialLoginSerializer

class NaverLogin(SocialLoginView):
    adapter_class = NaverOAuth2Adapter
    callback_url = NAVER_CALLBACK_URI
    client_class = OAuth2Client
    serializer_class = SocialLoginSerializer

