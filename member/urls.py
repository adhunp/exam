from django.urls import path
from .import views
app_name='member'
urlpatterns=[
             path('mhome',views.mhome,name = 'mhome'),
             path('m_login',views.m_login,name = 'm_login'),
             path('viewwork',views.viewwork,name = 'viewwork'),
             path('viewproject',views.viewproject,name = 'viewproject'),
             path('mpsw',views.mpsw,name = 'mpsw'),
             path('update/<int:eid>',views.update,name = 'update'),

]