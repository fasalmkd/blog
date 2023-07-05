from django.urls import path
from.import views

urlpatterns=[
    path("",views.index,name="index"),
    path("post/<int:id>/",views.post,name="post"),
    path("delete/<int:id>/",views.delete,name="delete"),
    path("edit/<int:id>/",views.edit,name="edit"),
    path("add",views.add,name="add"),
    path("register", views.register, name="register")
]