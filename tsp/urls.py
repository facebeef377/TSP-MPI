from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
from . import views
from .models import Task, Instance, History
from rest_framework import routers, serializers, viewsets
from django.conf.urls import url, include


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()

urlpatterns = [
    url(r'^$', views.task_run, name='task_run'),

    url(r'^start/', views.check_tasks, name='start'),
    url(r'^getdata/', views.get_data, name='get_data'),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^tasks/$', CreateView.as_view(), name="create"),
    url('^tasks/(?P<owner_id>.+)/$', UserTaskList.as_view()),
    url(r'^instances/$', CreateView_Instance.as_view(), name="create"),
    url('^instances/(?P<owner_id>.+)/$', UserTaskList_Instance.as_view()),
    url(r'^history/$', CreateView_History.as_view(), name="create"),
    url('^history/(?P<owner_id>.+)/$', UserTaskList_History.as_view()),
]
