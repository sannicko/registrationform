from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = [
             	url(r'^register/$', UserSignUpView.as_view(),name="user_signup"),
            	url(r'login/$', LoginView.as_view(),name="user_login"),
            	url(r'home/$', UserHome.as_view(),name="user_home"),

            	#url(r'profile/$', UserProfile.as_view(),name="user_profile"),

            	# url(r'addFriend/$', NewFriend.as_view(),name="add_friend"),
            	
            	url(r'submitForm$',form_submit, name="submit_form"),

            	#url(r'removeFriend/$',RemoveFriend.as_view(),name="remove_friend"),
            	url(r'logout/$', LogoutView,name="user_logout"),
             ]