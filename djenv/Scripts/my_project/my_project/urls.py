"""my_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from my_app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^department', views.department),
    url(r'^dependent', views.dependent),
    url(r'^deplocation', views.deplocation),
    url(r'^$', views.employee),
    url(r'^project', views.project),
    url(r'^workson', views.workson),

    url(r'^sel1', views.sel1),
    url(r'^sel2', views.sel2),
    url(r'^sel3', views.sel3),
    url(r'^sel4', views.sel4),
    url(r'^sel5', views.sel5),
    url(r'^sel6', views.sel6),

    url(r'^delete_employee', views.delete_employee),
    url(r'^delete_department', views.delete_department),
    url(r'^delete_deplocation', views.delete_deplocation),
    url(r'^delete_project', views.delete_project),
    url(r'^delete_workson', views.delete_workson),
    url(r'^delete_dependent', views.delete_dependent),

    url(r'^init', views.init),
]