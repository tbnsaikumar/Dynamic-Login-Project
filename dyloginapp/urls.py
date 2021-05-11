from django.conf.urls import url
from . import views
urlpatterns=[
        url(r'^$',views.input),
        url(r'^dylogin$',views.output)
]
