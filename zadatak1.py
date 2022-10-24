def fn(ls):
    """
    Funkcija prima listu stringova predmeta. Provjeri je li lista i jesu li svi
    stringovi ako ne error. Kreira dictionary gdje je key index, a value obrnuti
    string (One-liner u return-u)
    """
    # return({_: item for item in ls if isinstance(ls, list) and isinstance(item, str)})
    assert isinstance(x, list) and all([isinstance(i, str) for i in ls])
    return {k:v[::-1] for k, v in enumerate(ls)}

print(fn(["Stol", "Stolica", "Krevet", "Fotelja"]))