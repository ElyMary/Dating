from django.urls import path
from . import views
from .views import bulkupload

urlpatterns = [
    path('', views.insert_emp, name='insert-emp'),
    path('show/', views.show_emp, name='show-emp'),
    path('edit/<int:pk>', views.edit_emp, name='edit-emp'),
    path('remove/<int:pk>', views.remove_emp, name='remove-emp'),
    # path('bulkupload/<int:pk>',views.bulkupload, name='bulkupload'),
    path('',views.bulkupload, name='bulkupload'),
]