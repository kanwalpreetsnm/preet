
from django.conf.urls import url
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

namespace="vedio"

urlpatterns = [
    path('',views.categorylist,name='catlist'),
    path('postcomment',views.comment,name='postcomment'),
    path('<slug:slug>',views.videodetail,name='videodetail'),
    path('<slug:slug>/',views.categoryvedio,name='catvedio'),

]