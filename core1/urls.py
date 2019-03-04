from django.urls import path
from .views import abc1,empdetail,empdelete,emp_form,emp_update
urlpatterns=[
    path('',abc1,name="abc1"),
    path('empdetail/<int:pk>',empdetail,name="empdetail"),
    path('empdetail/delete/<int:pk>',empdelete,name="empdelete"),
    path('empdetail/create',emp_form,name="emp_form"),
    path('empdetail/update/<int:pk>',emp_update,name="emp_update")


]