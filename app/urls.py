from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('app.routes.index')),
]

handler404 = "app.views.page_not_found_view"
