from django.shortcuts import render, redirect
from .models import Uzytkownik
from .forms import UzytkownikForm
from .forms import WniosekUrlForm
from .models import Wniosek_url, Uzytkownik
from django.utils import timezone
from .forms import ZawiadomienieForm
from django.utils.timezone import now
from .forms import EwidencjaForm
from .models import Ewidencja_cp
from .forms import LoginForm
from .models import Logowanie, Uzytkownik



# Widok do wyświetlania listy użytkowników
def lista_uzytkownikow(request):
    uzytkownicy = Uzytkownik.objects.all()
    return render(request, 'lista_uzytkownikow.html', {'uzytkownicy': uzytkownicy})

# Widok do dodawania nowego użytkownika
def dodaj_uzytkownika(request):
    if request.method == 'POST':
        form = UzytkownikForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  # Po dodaniu użytkownika przekierowanie na stronę główną
    else:
        form = UzytkownikForm()
    return render(request, 'dodaj_uzytkownika.html', {'form': form})
    
    
def panel_pracownika(request):
    return render(request, 'pracownik/panel_pracownika.html')  # Domyślnie Ewidencja godzin pracy


def zawiadomienie(request):
    return render(request, 'pracownik/zawiadomienie.html')

def ewidencja(request):
    return render(request, 'pracownik/ewidencja.html')

def przeglad(request):
    return render(request, 'pracownik/przeglad.html')
    
    
def wniosek_urlop(request):
    # Pobranie ID zalogowanego użytkownika z sesji
    user_id = request.session.get('user_id')

    # Jeśli użytkownik nie jest zalogowany, przekieruj na stronę logowania
    if not user_id:
        return redirect('login')

    if request.method == 'POST':
        form = WniosekUrlForm(request.POST)
        if form.is_valid():
            wniosek = form.save(commit=False)
            # Ustawiamy dodatkowe wartości
            wniosek.status = 'Oczekujący'
            wniosek.data_zalozenia = now()
            wniosek.Uzytkownik_id_uzytkownika = user_id  # Przypisanie do zalogowanego użytkownika
            wniosek.save()
            return redirect('/pracownik/przeglad/')  # Przekierowanie po zapisaniu
    else:
        form = WniosekUrlForm()

    return render(request, 'pracownik/wniosek_urlop.html', {'form': form})
    
    
def zawiadomienie(request):
    # Pobranie ID zalogowanego użytkownika z sesji
    user_id = request.session.get('user_id')

    # Jeśli użytkownik nie jest zalogowany, przekieruj na stronę logowania
    if not user_id:
        return redirect('login')

    if request.method == 'POST':
        form = ZawiadomienieForm(request.POST)
        if form.is_valid():
            zawiadomienie = form.save(commit=False)
            # Ustawiamy dodatkowe wartości dla zawiadomienia
            zawiadomienie.status = 'Zgłoszone'
            zawiadomienie.data_zalozenia = now()
            zawiadomienie.Uzytkownik_id_uzytkownika = user_id  # Przypisanie do zalogowanego użytkownika
            zawiadomienie.save()
            return redirect('/pracownik/przeglad/')  # Przekierowanie po zapisaniu
    else:
        form = ZawiadomienieForm()

    return render(request, 'pracownik/zawiadomienie.html', {'form': form})  



def przeglad(request):
     # Pobranie ID zalogowanego użytkownika z sesji
    user_id = request.session.get('user_id')

    # Jeśli użytkownik nie jest zalogowany, przekieruj na stronę logowania
    if not user_id:
        return redirect('login')

    # Pobierz dane użytkownika
    try:
        uzytkownik = Uzytkownik.objects.get(id_uzytkownika=user_id)
    except Uzytkownik.DoesNotExist:
        uzytkownik = None

    # Pobierz zgłoszenia użytkownika
    zgłoszenia = Wniosek_url.objects.filter(Uzytkownik_id_uzytkownika=user_id)

    return render(request, 'pracownik/przeglad.html', {
        'uzytkownik': uzytkownik,
        'zgloszenia': zgłoszenia,
    })
    
    
    
def ewidencja(request):
    # Pobranie ID zalogowanego użytkownika z sesji
    user_id = request.session.get('user_id')

    # Jeśli użytkownik nie jest zalogowany, przekieruj na stronę logowania
    if not user_id:
        return redirect('login')

    # Obsługa dodawania wpisu
    if request.method == 'POST':
        form = EwidencjaForm(request.POST)
        if form.is_valid():
            wpis = form.save(commit=False)
            wpis.Uzytkownik_id_uzytkownika = user_id
            wpis.save()
            return redirect('ewidencja')  # Odświeżenie strony po dodaniu wpisu
    else:
        form = EwidencjaForm()

    # Pobieranie danych dla bieżącego miesiąca
    today = now().date()
    wpisy = Ewidencja_cp.objects.filter(
        Uzytkownik_id_uzytkownika=user_id,
        data__month=today.month,
        data__year=today.year
    ).order_by('data')

    return render(request, 'pracownik/ewidencja.html', {'form': form, 'wpisy': wpisy})  
    
    
    
# def login_view(request):
    # error_message = None
    # if request.method == 'POST':
        # form = LoginForm(request.POST)
        # if form.is_valid():
            # login = form.cleaned_data['login']
            # haslo = form.cleaned_data['haslo']

            # # Weryfikacja danych logowania
            # try:
                # logowanie = Logowanie.objects.get(login=login, haslo=haslo)
                # user = Uzytkownik.objects.get(id_uzytkownika=logowanie.id_uzytkownika)
                # # Zapisz zalogowanego użytkownika w sesji
                # request.session['user_id'] = user.id_uzytkownika
                # return redirect('/pracownik/')  # Przekierowanie do panelu pracownika
            # except Logowanie.DoesNotExist:
                # error_message = "Nieprawidłowy login lub hasło."
            # except Uzytkownik.DoesNotExist:
                # error_message = "Nie znaleziono użytkownika powiązanego z tym loginem."
    # else:
        # form = LoginForm()

    # return render(request, 'logowanie.html', {'form': form, 'error_message': error_message})   


def login_view(request):
    error_message = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            login = form.cleaned_data['login']
            haslo = form.cleaned_data['haslo']

            # Weryfikacja danych logowania
            try:
                logowanie = Logowanie.objects.get(login=login, haslo=haslo)
                user = Uzytkownik.objects.get(id_uzytkownika=logowanie.id_uzytkownika)
                # Zapisz zalogowanego użytkownika w sesji
                request.session['user_id'] = user.id_uzytkownika
                return redirect('/pracownik/panel_pracownika/')  # Przekierowanie do panelu pracownika
            except Logowanie.DoesNotExist:
                error_message = "Nieprawidłowy login lub hasło."
            except Uzytkownik.DoesNotExist:
                error_message = "Nie znaleziono użytkownika powiązanego z tym loginem."
    else:
        form = LoginForm()

    return render(request, 'pracownik/logowanie.html', {'form': form, 'error_message': error_message})


    
    
def pracownik_panel(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('/')  # Przekierowanie na stronę logowania, jeśli użytkownik nie jest zalogowany

    # Pobierz dane użytkownika
    try:
        user = Uzytkownik.objects.get(id_uzytkownika=user_id)
    except Uzytkownik.DoesNotExist:
        return redirect('/')  # Przekierowanie, jeśli użytkownik nie istnieje

    return render(request, 'pracownik/panel.html', {'user': user})
    
    
def logout_view(request):
    # Usunięcie sesji użytkownika
    if 'user_id' in request.session:
        del request.session['user_id']
    return redirect('/')  # Przekierowanie na stronę główną
    

    