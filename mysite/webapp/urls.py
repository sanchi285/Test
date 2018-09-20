from django.conf.urls import url
from . import views
urlpatterns =[
    url(r'^$',views.index,name='index'),
    url(r'^contact/',views.contact,name='contact'),
    url(r'^info/',views.info,name='info'),
    url(r'^stu/',views.studentForms,name='stu'),
    url(r'^sub_it/',views.studentForms,name='stu'),
    url(r'^writeI/',views.fileWrite,name='writeI')
    
    ]
