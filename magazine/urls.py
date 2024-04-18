from os import name
from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Uncomment the next line to enable the admin:
    path('',views.index, name="index"),
]
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
