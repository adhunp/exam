from django.urls import path
from .import views
app_name='header'
urlpatterns=[
            path('hlogin',views.hlogin,name = 'hlogin'),
            path('h_home',views.h_home,name = 'h_home'),
            path('employee',views.employee,name = 'employee'),
            path('viewemp',views.viewemp,name = 'viewemp'),
            path('leader',views.leader,name = 'leader'),
            path('project',views.project,name = 'project'),
            path('eg',views.eg,name = 'eg'),
]