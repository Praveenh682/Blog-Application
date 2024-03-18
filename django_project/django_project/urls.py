
from django.conf import settings
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views
from django.conf.urls.static import static
from django.urls import path
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls), 
    path("register/", user_views.register, name="register"),
    path("profile/", user_views.profile, name="profile"),
    path("login/", auth_views.LoginView.as_view(template_name='users/login.html',redirect_authenticated_user=True), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
    # path('logout/', CustomLogoutView.as_view(), name='logout'),
    path("", include('blog.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)




