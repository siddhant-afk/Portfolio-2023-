
from django.urls import path
from .views import blogs
urlpatterns = [

    path("",blogs,name="all_blogs"),
]

