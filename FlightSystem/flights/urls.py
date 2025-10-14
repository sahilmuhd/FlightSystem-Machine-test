from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add/', views.add_route, name='add_route'),
    path('find-nth/', views.find_nth_node, name='find_nth'),
    path('longest/', views.longest_node, name='longest'),
    path('shortest/', views.shortest_node, name='shortest'),

]
