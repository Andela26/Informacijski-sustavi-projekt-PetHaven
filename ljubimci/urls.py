from django.urls import path
from . import views
from .views import UrediLjubimca, ObrisiLjubimca, PopisLjubimaca


urlpatterns = [
    path("", views.lista_ljubimaca, name="lista_ljubimaca"),
    path("novi/", views.novi_ljubimac, name="novi_ljubimac"),
    path("<int:pk>/", views.detalji_ljubimca, name="detalji_ljubimca"),
    path("<int:pk>/uredi/", UrediLjubimca.as_view(), name="uredi_ljubimca"),
    path("<int:pk>/obrisi/", ObrisiLjubimca.as_view(), name="obrisi_ljubimca"),
    path("", PopisLjubimaca.as_view(), name='popis_ljubimaca'),

    path("<int:pk>/zapis/novi/", views.novi_zapis, name="novi_zapis"),
    path("zapis/<int:pk>/uredi/", views.uredi_zapis, name="uredi_zapis"),
    path("zapis/<int:pk>/obrisi/", views.obrisi_zapis, name="obrisi_zapis"),
]


