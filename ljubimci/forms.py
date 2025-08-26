from django import forms
from .models import Ljubimac, ZdravstveniZapis, Aktivnost, Obrok

class LjubimacForm(forms.ModelForm):
    class Meta:
        model = Ljubimac
        fields = ["ime_ljubimca", "vrsta_ljubimca", "datum_rodenja_ljubimca"]

class ZdravstveniZapisForm(forms.ModelForm):
    class Meta:
        model = ZdravstveniZapis
        fields = [
            "datum",
            "tezina_ljubimca",
            "sva_cjepiva_primljena",
            "bolesti",
            "lijekovi",
            "opis",
        ]

class AktivnostForm(forms.ModelForm):
    class Meta:
        model = Aktivnost
        fields = ["vrsta_aktivnosti", "datum_aktivnosti", "trajanje_aktivnosti"]

class ObrokForm(forms.ModelForm):
    class Meta:
        model = Obrok
        fields = ["vrijeme_obroka", "vrsta_hrane"]
