from django.urls import path

from . import views

#url conf
urlpatterns = [
    path('hello/', views.say_hello),
    path('brian/', views.brian, name = "brian"),
    path('david/', views.david, name = "david"),
    path("<str:name>", views.greet, name = "greet")
]
