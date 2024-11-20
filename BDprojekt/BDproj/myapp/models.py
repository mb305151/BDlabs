from django.db import models
from django.utils import timezone


class Uzytkownik(models.Model):
    id_uzytkownika = models.IntegerField(primary_key=True)
    imie = models.CharField(max_length=20)
    nazwisko = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    rola_id_rola = models.IntegerField()
    ilosc_dni_urlopowych = models.IntegerField(null=True, blank=True)
    zalegly_urlop = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = "Uzytkownik"
        managed = False  # Django nie zarządza tą tabelą

class Wniosek_url(models.Model):
    id_wniosek = models.AutoField(primary_key=True)  # Automatyczne generowanie unikalnych wartości
    data_poczatkowa = models.DateField()
    data_koncowa = models.DateField()
    status = models.CharField(max_length=20, default='Oczekujący')
    data_zalozenia = models.DateField(default=timezone.now)
    Uzytkownik_id_uzytkownika = models.IntegerField()

    class Meta:
        db_table = 'wniosek_url'  # Nazwa istniejącej tabeli
        managed = False  # Django NIE będzie zarządzać tabelą



class Ewidencja_cp(models.Model):
    id_ewidencji = models.AutoField(primary_key=True)
    data = models.DateField()
    godziny_pracy = models.IntegerField()
    Uzytkownik_id_uzytkownika = models.IntegerField()

    class Meta:
        db_table = 'ewidencja_cp'
        managed = False  # Korzystamy z istniejącej tabeli


class Logowanie(models.Model):
    id_logowania = models.AutoField(primary_key=True)
    id_uzytkownika = models.IntegerField()
    login = models.CharField(max_length=50)
    haslo = models.CharField(max_length=50)

    class Meta:
        db_table = 'logowanie'
        managed = False  # Korzystamy z istniejącej tabeli
