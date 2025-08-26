# PetHaven web servis

Za izradu ovog projekta korišteni su Python, HTML, CSS, Chart.js, SQLite i Docker.

Ova aplikacija omogućuje korisnicima da prate najbitnije informacije o zdravlju svojih kućnih ljubimaca, kao što su veterinarski pregledi, cijepljenja, lijekovi i slično.

U aplikaciji je moguće izvoditi sljedeće CRUD funkcionalnosti: unošenje podataka o kućnim ljubimcima, uređivanje i brisanje tih podataka te pregled svih do sada zabilježenih ljubimaca. Također je moguće unijeti za ljubimca podatke o veterinarskim pregledima i općenitom zdravlju, uređivati i brisati te podatke, te dobiti pregled svih zdravstvenih zapisa za pojedinog ljubimca. Kada korisnik klikne na ime ljubimca otvore mu se svi do tada zabilježeni podaci o tom ljubimcu, te ako je za ljubimca u više od jednog navrata izmjerena težina prikazati će se graf težine ljubimca kroz vrijeme.

## Kako pokrenuti aplikaciju Dockerom:
    1. Instalirati Docker Desktop.
    2. Pokrenuti Git Bash i ući u root projekta.
    3. Izvršiti naredbu: docker build -t ljubimci:latest .
    4. Inicijalizirati bazu naredbom: docker run --rm -it ljubimci:latest python manage.py migrate
    5. Pokrenuti server naredbom: docker run --name ljubimci -p 5001:8080 ljubimci:latest
    6. Otvoriti aplikaciju na linku: http://localhost:5001/

## Kako pokrenuti aplikaciju lokalno bez Dockera:
    1. Instalirati Python 3.13 i Git Bash.
    2. Pokrenuti Git Bash i klonirati repozitorij naredbom: git clone https://github.com/Andela26/Informacijski-sustavi-projekt-PetHaven
    3. Kreirati virtualno okruženje naredbom: - za Windows
                                            python -m venv .venv
                                            .venv\Scripts\activate
                                            - za Linux/macOS
                                            python3 -m venv .venv
                                            source .venv/bin/activate
    4. Instalirati dependencies naredbom: pip install -r requirements.txt
    5. Inicijalizirati bazu naredbom: python manage.py migrate
    6. Pokrenuti server naredbom: python manage.py runserver
    7. Otvoriti aplikaciju na linku: http://127.0.0.1:8000