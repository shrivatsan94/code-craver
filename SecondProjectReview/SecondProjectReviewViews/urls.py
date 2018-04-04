'''
Created on 03-Apr-2018

@author: Owner
'''
from django.conf.urls import url
from SecondProjectReviewViews import WelcomePageView, LoginPageView,SignUpPageView


urlpatterns=[
    url(r'^$', WelcomePageView.index,name='Welcome Page'),
    url(r'^login', LoginPageView.index,name='Login Page'),
    url(r'^signup', SignUpPageView.index,name='signup Page'),
    ]