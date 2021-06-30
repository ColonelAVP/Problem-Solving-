# fn to check if a string is Pangram or not

def ispangram(string1):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in string1.lower():
            return False
    return True

string1 = "abcdefghijklmnopqrstuvxyz"
ispangram(string1)

if ispangram(string1):
    print("")


