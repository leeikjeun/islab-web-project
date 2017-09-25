from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^Lab_intro/', views.Lab_intro, name='Lab_intro'),
    url(r'^Profe_intro/', views.Profe_intro, name='Profe_intro'),
    url(r'^Unknown_post/', views.Unknown_post, name='Unknown_post'),
    url(r'^Profe_info/', views.Profe_info, name='Profe_info'),
    url(r'^GGul_tip/', views.GGul_tip, name='GGul_tip'),
    url(r'^jokbo/', views.jokbo, name='jokbo'),
    url(r'^report/', views.report, name='report'),
    url(r'^mypage/', views.mypage, name='mypage'),

]
