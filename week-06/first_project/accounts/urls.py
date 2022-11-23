from django.urls import path

from accounts.views import hello, signup, SignupView, SignupFormView, LoginView

app_name = 'accounts'

urlpatterns = [
    path('hello/<str:name>/', hello),
    path('signup/', SignupFormView.as_view()),
    path('login/', LoginView.as_view()),
]
