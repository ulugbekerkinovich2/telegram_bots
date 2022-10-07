from django.urls import path

from basic_app import views

urlpatterns = [
    path('anketa/', views.ListAnketa.as_view()),
    path('anketa/<int:pk>', views.DetailAnketa.as_view()),
    path("elon_shogird/", views.List_Elon_Shogird.as_view()),
    path("elon_shogird/<int:pk>", views.Detail_Elon_Shogird.as_view()),
    path("elon_ustoz/", views.List_Elon_Ustoz.as_view()),
    path("elon_ustoz/<int:pk>", views.Detail_Elon_Ustoz.as_view()),
    path("elon_sherik/", views.List_Elon_Sheirk.as_view()),
    path("elon_sherik/<int:pk>", views.Detail_Elon_Sherik.as_view()),
    path("elon_xodim/", views.List_Elon_Hodim.as_view()),
    path("elon_xodim/<int:pk>", views.Detail_Elon_Hodim.as_view()),
    path("elon_ish/", views.List_Elon_Ish_Joyi.as_view()),
    path("elon_ish/<int:pk>", views.Detail_Elon_ish_joyi.as_view()),
]
