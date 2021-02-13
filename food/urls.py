from django.urls import path

from . import views
from food.views import CreatePostView

urlpatterns = [
    path('', CreatePostView.as_view(), name='add_post'),
    path('result/', views.index, name='index'),
]