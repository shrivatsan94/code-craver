'''
Created on 23-Mar-2018

@author: Owner
'''
#from MyApp.urls import urlpatterns
from django.conf.urls import url
from MyApplication import views, SignUpView,SignedUpView


urlpatterns=[
    url(r'^$', views.index,name='index'),
    url(r'^signup', SignUpView.index,name='signup'),
    url(r'^signedUp', SignedUpView.index,name='signedup'),
    ]