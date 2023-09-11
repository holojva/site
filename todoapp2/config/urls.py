"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from todo.views import index_view, status_view, deleting_done_view, goodbye_data_view, edit_view, delete_view, ask_to_delete_view, index_json_view, json_frontend_view
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index_view),
    path("status-change/<int:pk>/", status_view),
    path("delete-all-done/", deleting_done_view),
    path("goodbye-data/", goodbye_data_view),
    path("edit/<int:pk>", edit_view),
    path("ask_to_delete/<int:pk>", ask_to_delete_view),
    path("delete/<int:pk>", delete_view),
    path("json_simple", index_json_view, name="index-json"),
    path("json_frontend", json_frontend_view, name="json-frontend")
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)