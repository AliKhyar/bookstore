
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    ## admin 
    path('admin/', admin.site.urls),

    #auth
    path('accounts/', include('django.contrib.auth.urls')),

    #sign up
    path('accounts/', include('users.urls')),

    # pages app
    path('', include('pages.urls')),
]
