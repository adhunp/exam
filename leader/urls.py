from django.urls import path
from .import views
app_name='leader'
urlpatterns=[
            path('lhome',views.lhome,name = 'lhome'),
            path('tlogin',views.tlogin,name = 'tlogin'),
            path('vteam',views.vteam,name = 'vteam'),
            path('assign',views.assign,name = 'assign'),
            path('cpsw',views.cpsw,name = 'cpsw'),
            path('del_emp/<int:eid>',views.del_emp,name='del_emp'),
            path('delt',views.delt,name='del')
            
]