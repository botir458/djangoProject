from django.contrib.auth.views import LogoutView
from django.urls import path

from apps.views import MainTemplateView, LogintListView, StudentDetailw, RegisterWiever, LoginWieve, LoginWieve,updates

urlpatterns = [

    path('', MainTemplateView.as_view(), name='main_page'),

    path('logins', LogintListView.as_view(), name='logins'),

    # path('register', RegisterWiever.as_view(), name='register_wiever'),
    # path('login', LoginWieve.as_view(), name='login_wiever'),
    path('update', updates.as_view(), name='update'),
]
