def fn(dict1, dict2):
    """
    Funkcija prima dva jednostavna dictionary-a s ključevima valuta i cijene,
    gdje je lista vrijednosti key. Provjeri je su li oba paramentra dictionary
    ako ne error. Provjeri jesu li vrijednosti u oba dictionaryima liste, ako ne error. 
    Provjeri postoje li ključevi "valute" i "cijena", ako ne error.
    Kreira novu listu tupla u kojoj se nalaze samo elementi koji se ponavljaju u oba
    na istim indexima te imaju istu vrijednost (One-liner u return-u)
    """
    
    return([])


print(fn({"valute": ["GBP", "USD", "CZK", "Error"], "cijena": [8.5, 7.7, 0.3, 10.3]},
        {"valute": ["EUR", "USD", "CZK", "Error"], "cijena": [7.5, 7.7, 0.3, 5.5]}))