"""mapper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from .views import FilesAll, FilesContents, FilesDetail, FilesUpdate, FilesUpload


urlpatterns = [
    path("", FilesUpload.as_view(), name="files-upload"),
    path("files/", FilesAll.as_view(), name="files-all"),
    path("files/<int:pk>/", FilesDetail.as_view(), name="files-detail"),
    path("files/<int:pk>/contents/", FilesContents.as_view(), name="files-contents"),
    path("files/update/<int:pk>/", FilesUpdate.as_view(), name="files-update"),
]
