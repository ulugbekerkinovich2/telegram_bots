from django.urls import path

from basic_app import views

urlpatterns = [
    path('anketa/', views.ListAnketa.as_view()),
    path('anketa/<int:pk>', views.DetailAnketa.as_view())
]
