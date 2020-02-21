from django.urls import path

from . import views

app_name = 'tools'

urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),
    path('<int:pk>/', views.DetailView.as_view(), name = 'detail'),
    path('add/', views.CreateView.as_view(), name = 'create'),
    path('neighbors', views.NeighborView.as_view(), name = 'neighbors'),
    path('my_tools', views.MyToolView.as_view(), name = 'my_tools'),
    path('<int:pk>/edit', views.EditView.as_view(), name = 'edit'),
    path('<int:pk>/delete', views.DeleteView.as_view(), name = 'delete'),

]