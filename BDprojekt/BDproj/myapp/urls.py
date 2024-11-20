from django.urls import path
from . import views

urlpatterns = [
    path('dodaj/', views.dodaj_uzytkownika, name='dodaj_uzytkownika'),
    path('pracownik/panel_pracownika/', views.panel_pracownika, name='panel_pracownika'),  # Panel pracownika
    path('pracownik/zawiadomienie/', views.zawiadomienie, name='zawiadomienie'),  # Zawiadomienie o L4
    path('pracownik/ewidencja/', views.ewidencja, name='ewidencja'),  # Ewidencja godzin pracy
    path('pracownik/przeglad/', views.przeglad, name='przeglad'),  # Przegląd urlopów
    path('pracownik/wniosek_urlop/', views.wniosek_urlop, name='wniosek_urlop'),
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),


]
