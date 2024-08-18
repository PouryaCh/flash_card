from django.urls import path, include
from .  import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()

router. register('', views.UserListView)



# router = DefaultRouter()
# router.register('', views.UsersViewsetsView)

urlpatterns = [
    # path('', views.UsersGenericView.as_view()),
    # path('<int:pk>/', views.UsersDetailGenericView.as_view()),
    path('signup/', views.RegisterUserView.as_view()),
    path('login/', views.LoginUserView.as_view(), name='login'),
    path('auth/', obtain_auth_token, name='auth'),
    path('', include(router.urls))




]