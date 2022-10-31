from django.urls import path

from accounts.views import hello, signup

app_name = 'accounts'

urlpatterns = [
    path('hello/<str:name>/', hello),
    path('signup/', signup),
]
