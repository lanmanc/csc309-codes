from django.urls import path

from accounts.views import hello, signup, SignupView, SignupFormView, LoginView
from rest_framework_simplejwt.views import TokenObtainPairView


app_name = 'accounts'

urlpatterns = [
    path('hello/<str:name>/', hello),
    path('signup/', SignupFormView.as_view()),
    path('login/', LoginView.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

]
