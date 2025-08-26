
from django.contrib import admin
from .models import Ljubimac, ZdravstveniZapis, Aktivnost, Obrok

@admin.register(Ljubimac)
class LjubimacAdmin(admin.ModelAdmin):
    list_display = ('ime_ljubimca', 'vrsta_ljubimca', 'datum_rodenja_ljubimca')

@admin.register(ZdravstveniZapis)
class ZdravstveniZapisAdmin(admin.ModelAdmin):
    list_display = ('ljubimac', 'datum', 'tezina_ljubimca', 'sva_cjepiva_primljena')

@admin.register(Aktivnost)
class AktivnostAdmin(admin.ModelAdmin):
    list_display = ('ljubimac', 'vrsta_aktivnosti', 'datum_aktivnosti', 'trajanje_aktivnosti')

@admin.register(Obrok)
class ObrokAdmin(admin.ModelAdmin):
    list_display = ('ljubimac', 'vrsta_hrane', 'vrijeme_obroka')

