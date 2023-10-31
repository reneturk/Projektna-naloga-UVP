# Projektna naloga UVP - Analiza avtomobilskih oglasov iz podstrani zadnjih 100 oglasov na protalu avto.net iz dne 26. 10. 2023

### Rene Turk

V tej projektni nalogi sem preučeval oglase na spletni strani avto.net, in sicer na postrani [zadnjih 100 oglasov](https://www.avto.net/Ads/results_100.asp?oglasrubrika=1&prodajalec=2). Ker sem html kodo iz te strani pobral 26. 10. 2023,
sem potem tudi analizo naredil glede na takratne podatke. 

Najprej sem iz spletnega portala s pomočjo requests knjižnice pobral izvorno html kodo. Ker klasičen način ni deloval (dobival sem napako 403), sem se moral znajti 
z uporabo t.i. headerja. Nato sem iz html kode izluščil podatke. Za vsak oglas sem pridobil: ime oglasa/avtomobila, leto prve registracije, število prevoženih kilometrov, gorivo, tip menjalnika, moč motorja v konjskih močeh in ceno. Ker so se podatki
nahajali med različnimi html značkami, sem ime oglasov in cene za vsak oglas dal v svoj seznam, druge podatke pa sem dal skupaj v en seznam. Iz podatkov sem odstranil tudi enote, da sem pri analizi podatkov lahko te razvrščal po velikosti.

Nato je sledila izdelava slovarja, za katerega sem se odločil, ker so se nekateri podatki v html kodi za oglase z oznako 'top ponudba' dvakrat ponovili, nekateri oglasi niso imeli podatka o prevoženih kilometrih, oglasi pri 
električnih avtomobilih pa so imeli še podatek o moči baterije (ki sem ga iz analize izpustil). Vsak oglas pa je imel podatek o letu prve registracije, glede na katerega sem nato ločil podatke na posamezne podslovarje. 
Iz slovarja sem pridelal csv datoteko, iz katere sem nato analiziral podatke. Funkcije sem posebej pisal v svojo datoteko *funkcije.py*

Pri analizi sem podatke najprej s pomočjo knjižnice pandas dal v razpredelnico in jih razvrstil glede na različne vrednosti. Sledilo je še preučevanje podatkov; gledal sem povezave med različnimi vrednostmi, ter opazoval, kako
vplivajo ena na drugo.

Pri projektu so nastale naslednje datoteke:
- Zaradi boljše preglednosti sem v datoteko *funkcije.py* zapisoval funkcije in jih nato klical v Jupyter zvezek.
- V datoteki *pridobitev_csv_za_zadnjih_100.ipynb* je zapisan postopek pridelave csv datoteke.
- V tem postopku sta nastali datoteki *zadnjih_100.html* in *zadnjih_100.csv*. Prva je samo izvorna koda spletne strani, iz katere sem izluščil podatke, drugo pa sem pridelal in nato uporabil pri analizi.
- V datoteki *analiza_zadnjih_100.ipynb* pa sem naredil analizo podatkov.
