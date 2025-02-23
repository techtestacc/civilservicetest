"""
URL configuration for web_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from . import views
from .views import index, create_contact, get_contacts, edit_contact, delete_contact, create_contact_modal
urlpatterns = [
    path('', index, name="index"),
    path('contacts/', get_contacts, name='get_contacts'),
    path('contacts/createcontactmodal/<int:contact_id>', create_contact_modal, name='create_contact_modal'),
    path('contacts/createcontactmodal', create_contact_modal, name='create_contact_modal'),
    path('contacts/create', create_contact, name='create_contact'),
    path('contacts/edit/<int:contact_id>', edit_contact, name='edit_contact'),
    path('contacts/delete/<int:contact_id>/', delete_contact, name='delete_contact')

]
