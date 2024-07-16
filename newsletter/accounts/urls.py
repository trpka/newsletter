from django.urls import path
from .import  views

urlpatterns = [
    path("register/", views.register, name="register"),
    path(
        "company_register/",
        views.company_register.as_view(),
        name="company_register",
    ),
    path(
        "organization_register/",
        views.organization_register.as_view(),
        name="organization_register",
    ),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_view, name="logout"),
]
