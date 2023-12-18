"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: David Herman
email: david.herman@seznam.cz
discord: DavidHerman#5014
"""
# Texty k analýze
from TEXTS import TEXTS
# Registrovaní uživatelé a jejich hesla
users = {"bob":"123", "ann":"pass123", "mike":"password123", "liz":"pass123"} 

# Počet pomlček jako oddelovace
separator = "-" * 50 

# Přihlášení.
login = input("Enter your login: ").lower()
password = input("Enter your password: ")


if login in users.keys() and users[login] == password:
    # Přihlašovací údaje jsou správné.
    print(separator, f"Welcome to the app, {login}",f"We have {len(TEXTS)} texts to be analyzed.", separator, sep = "\n")   
else:
      # Přihlašovací údaje jsou špatné.
    print("Unregistered user, terminating the program..!")
    quit()

# Výběr textu k analýze
text_num = input(f"Enter a number (integer) btw. 1 and {len(TEXTS)} to select: ") 

if not text_num.isdigit():
    print("You did not select an integer, terminating the program..!")
    quit()
elif int(text_num) < 1 or int(text_num) > len(TEXTS):
    print("Your number is out of range, terminating the program..!")
    quit()
else:
    print (separator)

text_index = int(text_num) - 1

# index vybraného textu
sel_text = TEXTS[text_index]

# Rozdělení textu na jednotlivá slova a očištění slov od interpunkce
words = sel_text.split()
clear_words = []
for word in words:
    clear_words.append(word.strip(".,:;!?"))

# Počet slov v textu
print(f"There are {len(clear_words)} words in the selected text.")

# proměnné pro uložení jednotlivých slov
titlecase = []
uppercase = []
lowercase = []
numbers = []
words_length={}

for word in clear_words:
    if word.isalpha() and word.isupper():      # Nebere v potaz čísla v textu
        uppercase.append(word)  # Přidej ji do seznamu slov psaných velkým písmenem"
    elif word.isalpha() and word.islower():      # Nebere v potaz čísla v textu 
        lowercase.append(word)  # Přidej ji do seznamu slov psaných malým písmenem"
   
    if  word != word.lower() and word.isalpha():      # Nebere v potaz čísla v textu
        titlecase.append(word)  # Přidej ji do seznamu slov s velkým písmenem na začátku"
    elif word.isdigit():       
        numbers.append(int(word))  # Přidej ho do seznamu čísel"
 
    if len(word) not in words_length:    # Data pro graf
        words_length[len(word)] = 1
    else:
        words_length[len(word)] += 1

print(f"There are {len(titlecase)} titlecase words.")
print(f"There are {len(uppercase)} uppercase words.")
print(f"There are {len(lowercase)} lowercase words.")
print(f"There are {len(numbers)} numeric strings.")
print(f"The sum of all the numbers: {sum(numbers)}")

# Graf
max_range = int(max(words_length.keys())) + 1
max_space = int(max(words_length.values())) + 1

if max_space < 16:
    max_space = 16

print (separator)
print("LEN".rjust(5), "|   OCCURENCES", " " * (max_space - 16), "|NR.", sep=" ")
print(separator)

for key in range(1,max_range):
    if key in words_length.keys():
        space = max_space - words_length[key]
        print(str(key).rjust(5), "|", "*" * words_length[key], " " * space, "|", words_length[key], sep="")
print(separator)