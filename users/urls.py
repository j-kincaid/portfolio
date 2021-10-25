from django.conf.urls import url
from users.views import dashboard
# from django.contrib import admin

urlpatterns = [
    # url(r"^", include("users.urls")),
    # url(r"^admin/", admin.site.urls),
    # url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^dashboard/", dashboard, name="dashboard"),
]