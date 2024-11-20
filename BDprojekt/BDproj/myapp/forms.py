from django import forms
from .models import Uzytkownik
from .models import Wniosek_url
from .models import Ewidencja_cp

class UzytkownikForm(forms.ModelForm):
    class Meta:
        model = Uzytkownik
        fields = ['id_uzytkownika', 'imie', 'nazwisko', 'email', 'rola_id_rola', 'ilosc_dni_urlopowych', 'zalegly_urlop']
        
class WniosekUrlForm(forms.ModelForm):
    class Meta:
        model = Wniosek_url
        fields = ['data_poczatkowa', 'data_koncowa']
        widgets = {
            'data_poczatkowa': forms.DateInput(attrs={'type': 'date'}),
            'data_koncowa': forms.DateInput(attrs={'type': 'date'}),
        }        


class ZawiadomienieForm(forms.ModelForm):
    class Meta:
        model = Wniosek_url
        fields = ['data_poczatkowa', 'data_koncowa']
        widgets = {
            'data_poczatkowa': forms.DateInput(attrs={'type': 'date'}),
            'data_koncowa': forms.DateInput(attrs={'type': 'date'}),
        }
        
class EwidencjaForm(forms.ModelForm):
    class Meta:
        model = Ewidencja_cp
        fields = ['data', 'godziny_pracy']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
        }        
        
class LoginForm(forms.Form):
    login = forms.CharField(max_length=50, label="Login")
    haslo = forms.CharField(max_length=50, label="Hasło", widget=forms.PasswordInput)        