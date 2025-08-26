
from django.shortcuts import render, redirect, get_object_or_404
from .models import Ljubimac, ZdravstveniZapis, Aktivnost, Obrok
from .forms import LjubimacForm, ZdravstveniZapisForm, AktivnostForm, ObrokForm
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io, base64, urllib
import matplotlib.dates as mdates
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic import ListView, UpdateView, DeleteView
from django.urls import reverse_lazy


# ljubimci
def lista_ljubimaca(request):
    ljubimci = Ljubimac.objects.all()
    return render(request, "ljubimci/popis_ljubimaca.html", {"ljubimci": ljubimci})

def novi_ljubimac(request):
    if request.method == "POST":
        form = LjubimacForm(request.POST)
        if form.is_valid():
            ljubimac = form.save()
            return redirect("detalji_ljubimca", pk=ljubimac.pk)
    else:
        form = LjubimacForm()
    return render(request, "ljubimci/form.html", {"form": form})

def uredi_ljubimca(request, pk):
    ljubimac = get_object_or_404(Ljubimac, pk=pk)
    if request.method == "POST":
        form = LjubimacForm(request.POST, instance=ljubimac)
        if form.is_valid():
            form.save()
            return redirect("detalji_ljubimca", pk=pk)
    else:
        form = LjubimacForm(instance=ljubimac)
    return render(request, "ljubimci/uredi_ljubimca.html", {"form": form, "ljubimac": ljubimac})

def obrisi_ljubimca(request, pk):
    ljubimac = get_object_or_404(Ljubimac, pk=pk)
    if request.method == "POST":
        ljubimac.delete()
        return redirect("lista_ljubimaca")
    return render(request, "ljubimci/obrisi_ljubimca.html", {"ljubimac": ljubimac})

def detalji_ljubimca(request, pk):
    ljubimac = get_object_or_404(Ljubimac, pk=pk)
    zapisi = ljubimac.zapisi.all().order_by("datum")

    # graf težine
    pregledi = zapisi.order_by("datum")
    datumi = [p.datum for p in pregledi]
    tezine = [p.tezina_ljubimca for p in pregledi]
    
    # crtanje grafa samo ako ima vise od jednog zapisa
    if len(tezine) > 1: 
        fig, ax = plt.subplots()
        ax.plot(datumi, tezine, marker="o", linestyle="-")
        ax.set_title(f"Težina kroz vrijeme - {ljubimac.ime_ljubimca}")

        ax.set_xticks(datumi)  
        ax.set_yticks(tezine)  

        ax.xaxis.set_major_formatter(mdates.DateFormatter("%d.%m.%Y"))

        buf = io.BytesIO()
        plt.savefig(buf, format="png", bbox_inches="tight")
        buf.seek(0)
        string = base64.b64encode(buf.read())
        graf_uri = urllib.parse.quote(string)
        buf.close()
    else:
        graf_uri = None

    return render(request, "ljubimci/detalji_ljubimca.html", {
        "ljubimac": ljubimac,
        "zapisi": zapisi,
        "graf": graf_uri
    })

# zdravstveni zapisi
def novi_zapis(request, pk):
    ljubimac = get_object_or_404(Ljubimac, pk=pk)
    if request.method == "POST":
        form = ZdravstveniZapisForm(request.POST)
        if form.is_valid():
            zapis = form.save(commit=False)
            zapis.ljubimac = ljubimac
            zapis.save()
            return redirect("detalji_ljubimca", pk=pk)
    else:
        form = ZdravstveniZapisForm()
    return render(request, "zapisi/form.html", {"form": form, "ljubimac": ljubimac})

def uredi_zapis(request, pk):
    zapis = get_object_or_404(ZdravstveniZapis, pk=pk)
    if request.method == "POST":
        form = ZdravstveniZapisForm(request.POST, instance=zapis)
        if form.is_valid():
            form.save()
            return redirect("detalji_ljubimca", pk=zapis.ljubimac.pk)
    else:
        form = ZdravstveniZapisForm(instance=zapis)
    return render(request, "zapisi/form.html", {"form": form, "ljubimac": zapis.ljubimac})

def obrisi_zapis(request, pk):
    zapis = get_object_or_404(ZdravstveniZapis, pk=pk)
    ljubimac_pk = zapis.ljubimac.pk
    if request.method == "POST":
        zapis.delete()
        return redirect("detalji_ljubimca", pk=ljubimac_pk)
    return render(request, "zapisi/obrisi_zapis.html", {"zapis": zapis})


class PopisLjubimaca(ListView):
    model = Ljubimac
    template_name = "ljubimci/popis_ljubimaca.html"


class UrediLjubimca(UpdateView):
    model = Ljubimac
    form_class = LjubimacForm
    template_name = "ljubimci/uredi_ljubimca.html"

    def get_success_url(self):
        return reverse_lazy("detalji_ljubimca", kwargs={"pk": self.object.pk})


class ObrisiLjubimca(DeleteView):
    model = Ljubimac
    template_name = "ljubimci/brisanje_ljubimca.html"
    success_url = reverse_lazy("popis_ljubimaca")