from django.conf.urls import url
from app import views

urlpatterns = [
    url(r'^home/', views.home, name="home"),
    url(r'^signup/', views.signup, name="signup"),
    url(r'^get_name/', views.get_name, name="get_name"),
]
