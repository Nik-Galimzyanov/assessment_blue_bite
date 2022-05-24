from django.conf.urls import url

from .views import ObjectsHandlerView, GetObjectById, GetObjectByParams

urlpatterns = [
    url(r'^post_objects/', ObjectsHandlerView.as_view()),
    url(r'^get_obejct_by_id/(?P<object_id>[\w\d-]+)[/]?$', GetObjectById.as_view()),
    url(r'^get_obejct_by_params/', GetObjectByParams.as_view()),
]