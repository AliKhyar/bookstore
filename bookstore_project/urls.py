
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    ## admin 
    path('admin/', admin.site.urls),

    # User management
    path('accounts/', include('allauth.urls')), # new

    # pages app
    path('', include('pages.urls')),
]
