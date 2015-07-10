from django.conf.urls import url,include
from loginsys.views import IndexView

urlpatterns = [
    url(r'^logout/', 'loginsys.views.logout'),
    url(r'^login/', 'loginsys.views.login'),
    url(r'^register/', 'loginsys.views.register'),
    #url(r'^$', IndexView.as_view()),
]   