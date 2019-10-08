"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from webapp.views import IndexView, TrackerView, TrackerCreateView, TrackerUpdateView, \
    TrackerDeleteView, StatusView, TypeView, StatusCreateView, TypeCreateView, \
    StatusUpdateView, TypeUpdateView, StatusDeleteView, TypeDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('tracker/<int:pk>/', TrackerView.as_view(), name='tracker_view'),
    path('tracker/add/', TrackerCreateView.as_view(), name='tracker_add'),
    path('tracker/<int:pk>/update/', TrackerUpdateView.as_view(), name='tracker_update'),
    path('tracker/<int:pk>/delete/', TrackerDeleteView.as_view(), name='tracker_delete'),
    path('status/view/', StatusView.as_view(), name='status_view'),
    path('type/view/', TypeView.as_view(), name='type_view'),
    path('status/add/', StatusCreateView.as_view(), name='status_add'),
    path('type/add', TypeCreateView.as_view(), name='type_add'),
    path('status/<int:pk>/update/',StatusUpdateView.as_view(), name='status_update'),
    path('type/<int:pk>/update/', TypeUpdateView.as_view(), name='type_update'),
    path('status/<int:pk>/delete/', StatusDeleteView.as_view(), name='status_delete'),
    path('type/<int:pk>/delete/',TypeDeleteView.as_view(), name='type_delete'),

]


