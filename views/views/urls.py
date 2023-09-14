from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('views_app.urls')),
    path('captcha', include('captcha.urls')),
    path('accounts/', include('accounts.urls'))

]

