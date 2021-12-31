

from django.urls import path , re_path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('', views.FilmView)
router.register('accounts/profile', views.ProfileView)
# router.register('l', views.like)

app_name ='main'

urlpatterns = [
    path('v1/',include(router.urls)),
    path('v1/like/post',views.like,name='like'),
    path('v1/accounts/', include('accounts.urls')),
    # path('sendmail/',)
    # path('' ,views.index ,name='index'),
    # re_path(r'^get$', views.APIListCreateFilm.as_view() , name= 'apiFilmList'),
    # re_path(r'^update/(?P<pk>\d+)$', views.APIRetrieveUpdateDestroy.as_view() , name= 'apiFilmList'),

]