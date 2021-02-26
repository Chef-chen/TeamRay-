from django.urls import path
from . import views
urlpatterns = [
    # http://127.0.0.1:8000/v1/users/username
    path('<str:username>',views.UserView.as_view()),
    path('<str:username>/avatar',views.user_avatar),
    path('<str:username>/pic',views.user_pic),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]