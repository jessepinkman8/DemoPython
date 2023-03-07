from . import views
from django.urls import path

urlpatterns = [
    path('',views.demo,name='demo'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('cbvhome/',views.Tasklistview.as_view(),name='cbvhome'),
    path('detail/<int:pk>/',views.TaskDetailview.as_view(),name='detail'),
    path('asdupdate/<int:pk>/',views.TaskUpdateView.as_view(),name='asdupdate'),
    path('qwedelete/<int:pk>/',views.TaskDeleteView.as_view(),name='qwedelete'),

]
