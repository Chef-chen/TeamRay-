from django.urls import path
from . import views

urlpatterns = [
    path('<path:good_name>/list', views.Good_list),

    # http//:127.0.0.1:8000/v1/good/<user_id>
    path('<str:user_id>', views.GoodView.as_view()),

]
