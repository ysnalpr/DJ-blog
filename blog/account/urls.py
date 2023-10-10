from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from . import views

app_name = "account"

urlpatterns = [
    # login / logout / register urls
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("register/", views.register, name="register"),
    # change password urls
    path(
        "password-change/",
        auth_views.PasswordChangeView.as_view(
            success_url=reverse_lazy("account:password_change_done")
        ),
        name="password_change",
    ),
    path(
        "password-change/done/",
        auth_views.PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
    # password reset urls
    path(
        "password-reset/",
        auth_views.PasswordResetView.as_view(
            success_url=reverse_lazy("account:password_reset_done")
        ),
        name="password_reset",
    ),
    path(
        "password-reset/done/",
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "password-reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            success_url=reverse_lazy("account:password_reset_complete")
        ),
        name="password_reset_confirm",
    ),
    path(
        "password-reset/complete/",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
    # dashboard
    path("", views.dashboard, name="dashboard"),
]
