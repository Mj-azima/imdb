

from django.urls import path , re_path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('', views.UserView)

app_name ='main'

urlpatterns = [
    path('user/',include(router.urls))


]