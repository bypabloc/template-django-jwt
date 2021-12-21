from django.urls import path, include

urlpatterns = [
    path('user/', include('app.routes.UserRoutes')),
    path('auth/', include('app.routes.AuthRoutes')),
]
