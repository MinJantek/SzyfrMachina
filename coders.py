import random

matma = {
    "A" : 1,
    "Ą" : 1,
    "B" : 2,
    "C" : 3,
    "Ć" : 3,
    "D" : 4,
    "E" : 5,
    "Ę" : 5,
    "F" : 6,
    "G" : 7,
    "H" : 8,
    "I" : 9,
    "J" : 10,
    "K" : 11,   
    "L" : 12,
    "M" : 13,
    "N" : 14,
    "O" : 15,
    "Ó" : 15,
    "P" : 16,
    "R" : 17,
    "S" : 18,
    "Ś" : 18,
    "T" : 19,
    "U" : 20,
    "W" : 21,
    "Y" : 22,
    "Z" : 23
}

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
dictionary = {
        'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',   'E': '.',
        'F': '..-.',  'G': '--.',   'H': '....',  'I': '..',    'J': '.---',
        'K': '-.-',   'L': '.-..',  'M': '--',    'N': '-.',    'O': '---',
        'P': '.--.',  'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
        'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',  'Y': '-.--',
        'Z': '--..',  '0': '-----', '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
        '9': '----.', '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.',
        '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
        ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-',
        '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': ''
    }

def morsa(txt,code):

    reverse_dictionary = {v: k for k, v in dictionary.items()}


    coded = ""
    if code:
        for a in txt:
            if a.islower(): a = a.upper()
            if a in dictionary:
                coded += dictionary[a] + "/"
        coded = coded[:-1]
        return coded
    else:
        words = txt.split('//')
        result = []
        for word in words:
            morse_codes = word.split('/')
            letters = []
            for morse in morse_codes:
                if morse in reverse_dictionary:
                    letters.append(reverse_dictionary[morse])
            result.append(''.join(letters))
        
        return ' '.join(result)

    



reverse_matma = {}
for letter, number in matma.items():
    if number not in reverse_matma:
        reverse_matma[number] = letter

math_signs = ["+", "-", "*", ":"]

def matematyczny(txt: str, code: bool) -> str:
    if code:
        txt = txt.upper()
        numbers = []
        
        for char in txt:
            if char in matma:
                numbers.append(str(matma[char]))
        
        # Join numbers with random math signs as separators
        result = ""
        for i, num in enumerate(numbers):
            result += num
            if i != len(numbers) - 1:  # Don't add sign after last number
                result += random.choice(math_signs)
        
        return result
    
    else:
        # DECIPHER: Split by math signs to get individual numbers, then convert to letters
        cleaned = txt
        
        # Replace all math signs with a common separator (e.g., space)
        for sign in math_signs:
            cleaned = cleaned.replace(sign, " ")
        
        # Split by space to get individual numbers
        number_strings = cleaned.split()
        
        # Convert numbers back to letters
        result = ""
        for num_str in number_strings:
            if num_str.isdigit():
                num = int(num_str)
                if num in reverse_matma:
                    result += reverse_matma[num]
        
        return result




def ulamkowy(txt,code):
    return "4"
def komorkowy(txt,code):
    return "5"
def cezara(txt,code,trybe):
    return "6"



