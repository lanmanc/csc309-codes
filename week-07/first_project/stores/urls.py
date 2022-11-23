from django.urls import path

from stores.views import StoresView

app_name = 'stores'

urlpatterns = [
    path('list/', StoresView.as_view()),
]
