from django.urls import path
from . import views

urlpatterns = [
    # http//:127.0.0.1:8000/v1/good/<user_id>
    path('<str:user_id>', views.GoodView.as_view()),

]
