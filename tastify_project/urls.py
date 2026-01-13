from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from food.views import signup
from food.views import profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', include('food.urls')),  
    path('signup/', signup, name='signup'),
    path('profile/', profile, name='profile'),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(
    settings.STATIC_URL,
    document_root=settings.STATICFILES_DIRS[0]
)
