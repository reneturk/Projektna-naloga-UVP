#funkcija uredi_seznam naredi nov seznam, v katerega elemente prvotnega seznama, ki se dvakrat zapored ponovijo, napiše enkrat, 
#elemente, ki se trikrat ali štirikrat zapored ponovijo, napiše dvakrat, elemente, ki se samo enkrat, pa pusti pri miru. 

def uredi_seznam(seznam):
    nov_seznam = []
    ponovitve = 1

    for i in range(1, len(seznam)):
        if seznam[i] == seznam[i - 1]:
            ponovitve += 1
        else:
            if ponovitve == 2:
                nov_seznam.append(seznam[i - 1])
            elif ponovitve in (3, 4):
                nov_seznam.extend([seznam[i - 1]] * 2)
            else:
                nov_seznam.append(seznam[i - 1])
            ponovitve = 1

    if ponovitve == 2:
        nov_seznam.append(seznam[-1])
    elif ponovitve in (3, 4):
        nov_seznam.extend([seznam[-1]] * 2)
    else:
        nov_seznam.append(seznam[-1])

    return nov_seznam


#Funkcija, ki mi iz členov seznama, ki vsebuje podatek tipa npr. 3168 ccm, 184 kW / 250 KM izloči samo 250 KM.
def poberi_km(sez):
    for i in range(len(sez)):
        if '/' in sez[i]:
            sez[i] = sez[i][(-6):]
        if sez[i][0] == ' ':
            sez[i] = sez[i][1:]
    return sez

#Funkcija, ki pretvori elemente seznama, ki so v kW, v KM (1 kW = 1.341 KM) in zaokroži na najbližje celo število
def pretvorjeno_v_km(sez):
    for i in range(len(sez)):
        if sez[i][(-2):] == 'kW':
            sez[i] = sez[i][:(-2)]
            sez[i] = str(round(int(sez[i]) * 1.341)) + ' KM'
    return sez

#Funkcija, ki mi naredi seznam, v katerem so indeksi, na katerih se nahaja element a v seznamu sez
def na_katerih_indeksih_se_nahaja(sez, a):
    i = 0
    sez_indeksov = []
    for el in sez:
        if el == a:
            sez_indeksov.append(i)
        i += 1
    return sez_indeksov

#Funkcija, ki mi iz vseh nizov v seznamu tipa
#'AKCIJSKA CENA\n          \n\n\n\n\n\n            13.990 €\n           \n\n            13.690 €' in 
#'3.390 €\n           \n\n\n\n\n\n\n\n\n\n            oz. 51,00 EUR / mesec (*)'
#'35.999 €\n           \n\n            oz. 29.507 € + DDV(*)'
#izloči ceno

def poenostavi(sez):
    for i in range(len(sez)):
        if 'AKCIJSKA CENA\n' in sez[i]:
            sez[i] = sez[i][(-10):]
            while sez[i][0] ==  ' ':
                sez[i] = sez[i][1:]
        elif len(sez[i]) > 10:
            sez[i] = sez[i][:10]
            while sez[i][-1] == ' ' or sez[i][-1] == '\n':
                sez[i] = sez[i][:(-1)]
    return sez

#odstrani ' €' in '.' iz podatkov, da so primerni za kasnejšo obdelavo
def odstrani_cene(sez):
    for i in range(len(sez)):
        if ' €' in sez[i]:
            sez[i] = sez[i][:(-2)]
        if '.' in sez[i]:
            sez[i] = sez[i].replace('.','')
    return sez

#odstrani 'km', 'KM' iz podatkov, da so primerni za kasnejšo obdelavo
def odstrani_enote(sez):
    for i in range(len(sez)):
        if 'km' in sez[i] or 'KM' in sez[i]:
            sez[i] = sez[i][:(-3)]
    return sez