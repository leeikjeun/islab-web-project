from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^labintro/', views.Lab_intro, name='Lab_intro'),
    url(r'^profeintro/', views.Profe_intro, name='Profe_intro'),
    url(r'^unkownpost/', views.Unknown_post, name='Unknown_post'),
    url(r'^profeinfo/', views.Profe_info, name='Profe_info'),
    url(r'^profeinfo/leesangjun/', views.leesangjun, name='leesangjun'),
    url(r'^ggultip/', views.GGul_tip, name='GGul_tip'),
    url(r'^jokbo/', views.jokbo, name='jokbo'),
    url(r'^report/', views.report, name='report'),
    url(r'^mypage/', views.mypage, name='mypage'),
    url(r'^test/', views.test, name='test'),

]
