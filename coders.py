def endecypher(picked2,text1,text2):
    if picked2 == "frame8":
        szyfruj = False
        return f"('{text2}',{szyfruj})"
        code_type = eval(f"{picked}.code_name")
        text1 = eval(f"{code_type}('{text2}',szyfruj)")
    elif picked2 == "frame7":
        szyfruj = True
        a = f"('{text1}',{szyfruj})"
        print(a)
        return a
    





        code_type = eval(f"{picked}.code_name")
        text2 = eval(f"{code_type}('{text1}',szyfruj)")





def sylabowe(txt,code,tryb):
    return "1"
def morsa(txt,code):
    return "2"
def matematyczny(txt,code):
    return "3"
def ulamkowy(txt,code):
    return "4"
def komorkowy(txt,code):
    return "5"
def cezara(txt,code,tryb):
    return "6"