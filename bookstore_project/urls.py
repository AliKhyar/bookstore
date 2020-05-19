
from django.contrib import admin
from django.urls import path, include
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    ## admin 
    path('admin/', admin.site.urls),

    # User management
    path('accounts/', include('allauth.urls')), # new

    # pages app
    path('', include('pages.urls')),

    #books
    path('books/', include('books.urls')),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
