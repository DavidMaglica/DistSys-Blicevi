def fn(listOfDicts):
    """
    Funkcija uzima listu dictionarya proizvoda. Provjeri je li lsta
    i ako su svi dict ako ne error. Proizvod ima naziv, kategoriju i ocjenu
    Vraća dict s kategorijom za key i sumom ocjena (Jedan ili dva one linera)
    """
    # return({item["kategorija"]: "a", item["kategorija"]: "b"} for item in listOfDicts if isinstance(listOfDicts, list) and isinstance(item, dict))
    assert isinstance(listOfDicts, list)
    c = {k for d in listOfDicts for a, k in d.items() if a == "kategorija"}
    return{k:sum([v["ocjena"] for v in listOfDicts if v["kategorija"] == k]) for d in listOfDicts for _, k in d.items() if k in c}

print(fn([{"naziv": "Burek", "kategorija": "pite", "ocjena": 1},
        {"naziv": "Ramsteak", "kategorija": "steak", "ocjena": 9},
        {"naziv": "Ribeye", "kategorija": "steak", "ocjena": 4},
        {"naziv": "Sirnica", "kategorija": "pita", "ocjena": 5}]))