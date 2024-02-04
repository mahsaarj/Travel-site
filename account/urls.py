from django.urls import path
from . import views
app_name = 'account'
urlpatterns = [
    path('login', views.login_view,name='login'),
    #login
    #path('logout', views.logout_views, name='logout')
    #logout
    path('signup', views.signup_view, name='signup')
    #sign up / registeration
]