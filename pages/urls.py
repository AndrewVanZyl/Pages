from django.urls import path
from .views import HomePageView, AboutPageView, OtherPageView, MyPageView #new

urlpatterns = [
path('', HomePageView.as_view(), name='home'),
path('about/', AboutPageView.as_view(), name='about'), 
path('other/', OtherPageView.as_view(), name='other'),
path('mypage/', MyPageView.as_view(), name='mypage'),
]