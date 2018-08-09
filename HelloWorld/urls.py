from django.urls import path
from . import view
from . import pie
urlpatterns = [
    path('', view.hello),
    path('pie/',pie.hello)
    #path('world/', view.world)
]