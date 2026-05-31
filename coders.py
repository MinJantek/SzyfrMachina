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

def encypher(picked2):
    if picked2 == "frame8":
            return False
    elif picked2 == "frame7":
            return True







def sylabowe(txt, code, tryb):
    result = []
    
    for letter in txt:
        # Check if letter exists in the tryb (key)
        if letter.lower() in tryb.lower():
            # Find the position of the letter in tryb
            pos = tryb.lower().find(letter.lower())
            
            # Same rule for both encryption and decryption
            # Even position: shift +1
            # Odd position: shift -1
            if pos % 2 == 0:  # Even position
                new_pos = pos + 1
            else:  # Odd position
                new_pos = pos - 1
            
            # Check if new position is within bounds
            if 0 <= new_pos < len(tryb):
                new_letter = tryb[new_pos]
                # Preserve the original case
                if letter.isupper():
                    result.append(new_letter.upper())
                else:
                    result.append(new_letter.lower())
            else:
                # If out of bounds, keep original letter
                result.append(letter)
        else:
            # Letter not in tryb, leave unchanged
            result.append(letter)
    
    return ''.join(result)


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

