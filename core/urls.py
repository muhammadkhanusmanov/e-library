from django.contrib import admin
from django.urls import path
from api.views import UserView, RegisterView,LogView,Logout, Avatarka

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/',UserView.as_view()),
    path('signup/', RegisterView.as_view()),
    path('login/', LogView.as_view()),
    path('logout/', Logout.as_view()),
    path('addavatar/',Avatarka.as_view()),
    path('deleteavatar/',Avatarka.as_view()),
]
