from django.urls import path
from .views import CreateUser, BlacklistTokenView

app_name = 'user'

urlpatterns = [
    path('register/', CreateUser.as_view(), name='create_user'),
    path('logout/', BlacklistTokenView.as_view(), name='logout')
]