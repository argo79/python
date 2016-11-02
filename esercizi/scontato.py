def scontato(prezzo, sconto):
    prezzofinale=prezzo-(prezzo/100.0)*sconto
    return prezzofinale
print scontato(735, 15)
