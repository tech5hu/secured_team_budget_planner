
from django.contrib import admin
from django.urls import path, include
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('', user_views.home, name='home'),
    path('budgets/', include('budgets.urls')),
    path('login/', user_views.login_view, name='login'),
]

