from django.contrib import admin
from django.urls import path,include
from app import views


urlpatterns = [
    path("", views.index, name='index'),
    path("register/", views.register, name='register'),
    path("vote/", views.vote, name='vote' ),
    path("result/", views.result, name='result' ),
    path("update/", views.update, name='update' ),
    path("admin/voting_status/", views.voting_status, name='voting_status' ),
    # path("email/", views.email, name='email' ),
    # path("verify/", views.verify, name='verify' ),
]