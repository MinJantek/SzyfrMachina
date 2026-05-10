def endecypher(picked,picked2,text1,text2,trybe1,trybe2):
    if picked == "frame1":
        if picked2 == "frame8":
            szyfruj = False
            return f"('{text2}',{szyfruj},'{trybe1}')"
        elif picked2 == "frame7":
            szyfruj = True
            a = f"('{text1}',{szyfruj},'{trybe1}')"
            print(a)
            return a
    elif picked == "frame6":
        if picked2 == "frame8":
            szyfruj = False
            return f"('{text2}',{szyfruj},'{trybe2}')"
        elif picked2 == "frame7":
            szyfruj = True
            a = f"('{text1}',{szyfruj},'{trybe2}')"
            print(a)
            return a
    else:
        if picked2 == "frame8":
            szyfruj = False
            return f"('{text2}',{szyfruj})"
        elif picked2 == "frame7":
            szyfruj = True
            a = f"('{text1}',{szyfruj})"
            print(a)
            return a






def sylabowe(txt,code,trybe):
    return "1"
def morsa(txt,code):
    return "2"
def matematyczny(txt,code):
    return "3"
def ulamkowy(txt,code):
    return "4"
def komorkowy(txt,code):
    return "5"
def cezara(txt,code,trybe):
    return "6"