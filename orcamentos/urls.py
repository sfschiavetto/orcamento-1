from django.contrib import admin
from django.urls import path, include
from home.views import login 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path('', login, name='login'),
]

#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('login/', include('django.contrib.auth.urls')),
]
