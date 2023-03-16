from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.home, name = "home"),
    path("login", views.login, name = "login"),
    path("user", views.user_data, name = "userdata"),
    path("about", views.aboutus, name = "about"),
    path("family", views.family, name = "family"),
    path("charity", views.charity, name = "charity"),
    path("business", views.business, name = "business"),
    path("culture", views.culture, name = "culture"),
    path("bookevent", views.book_event, name="bookevent"),
    path("register", views.register, name = "register"),
    path("user_cart", views.usercart, name = "user_cart"),
    path("logout", views.logout, name = "logout"),
    path("change_pswd", views.change_password, name='change_pswd'),
    path('reset_password', auth_views.PasswordResetView.as_view(template_name = "password_reset_form.html"), name = "reset_password"),
    path('reset_password_sent',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name="password_reset_confirm"),
    path('password_reset_complete',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name="password_reset_complete"),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
