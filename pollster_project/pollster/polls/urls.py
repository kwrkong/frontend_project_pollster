from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>', views.detial, name='detail'),
    path('<int:question_id>/results/', views.detial, name='results'),
]