def fn(dict1, dict2):
    """
    Funkcija prima dva jednostavna dictionary-a s ključevima valuta i cijene,
    gdje je lista vrijednosti key. Provjeri je su li oba paramentra dictionary
    ako ne error. Provjeri jesu li vrijednosti u oba dictionaryima liste, ako ne error. 
    Provjeri postoje li ključevi "valute" i "cijena", ako ne error.
    Kreira novu listu tupla u kojoj se nalaze samo elementi koji se ponavljaju u oba
    na istim indexima te imaju istu vrijednost (One-liner u return-u)
    """
    # return([(x)] if isinstance(dict1, dict) and isinstance(dict2, dict))
    assert isinstance(dict1, dict) and isinstance(dict2, dict)
    assert all([isinstance(i, list) for _, i in dict1.items()] and all([isinstance(i, list) for _, i in dict2.items()]))
    assert (dict1.get("valute") and dict1.get("cijena") and dict2.get("valute") and dict2.get("cijena"))
    return [(a, b) for a, d, b, c in zip(dict1["cijena"], dict2["cijena"], dict1["valute"], dict2["valute"]) if (a == d) and (b == c)]

print(fn({"valute": ["GBP", "USD", "CZK", "Error"], "cijena": [8.5, 7.7, 0.3, 10.3]},
        {"valute": ["EUR", "USD", "CZK", "Error"], "cijena": [7.5, 7.7, 0.3, 5.5]}))