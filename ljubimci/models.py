from django.db import models

class Ljubimac(models.Model):
    ime_ljubimca = models.CharField(max_length=100)
    vrsta_ljubimca = models.CharField(max_length=100)
    datum_rodenja_ljubimca = models.DateField()

    def __str__(self):
        return self.ime_ljubimca

class ZdravstveniZapis(models.Model):
    ljubimac = models.ForeignKey(Ljubimac, on_delete=models.CASCADE, related_name="zapisi")
    datum = models.DateField()
    tezina_ljubimca = models.FloatField(null=True, blank=True)
    sva_cjepiva_primljena = models.BooleanField(default=False)
    bolesti = models.TextField(blank=True)
    lijekovi = models.TextField(blank=True)
    opis = models.TextField(blank=True)

    def __str__(self):
        return f"{self.ljubimac.ime_ljubimca} - {self.datum}"

class Aktivnost(models.Model):
    ljubimac = models.ForeignKey(Ljubimac, on_delete=models.CASCADE)
    vrsta_aktivnosti = models.CharField(max_length=100)
    datum_aktivnosti = models.DateField()
    trajanje_aktivnosti = models.IntegerField(help_text="Trajanje u minutama")

    def __str__(self):
        return f"{self.ljubimac.ime_ljubimca} - {self.vrsta_aktivnosti} ({self.datum_aktivnosti})"

class Obrok(models.Model):
    ljubimac = models.ForeignKey(Ljubimac, on_delete=models.CASCADE)
    vrijeme_obroka = models.TimeField()
    vrsta_hrane = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.ljubimac.ime_ljubimca} - {self.vrsta_hrane} ({self.vrijeme_obroka})"
