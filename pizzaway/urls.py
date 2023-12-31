#this mapps different urls to their views

from django.contrib import admin
from django.urls import path, include

from webinterface.views import set_language

urlpatterns = [
    path("", set_language),
    path("mitarbeiter/", include("employee.urls")),
    path("game/", include("game.urls")),
    path('admin/', admin.site.urls),
    path("<str:language_code>/", include("webinterface.urls")),
]
