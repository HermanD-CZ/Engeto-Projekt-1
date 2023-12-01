"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: David Herman
email: david.herman@seznam.cz
discord: DavidHerman#5014
"""
# Texty k analýze
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]
# Registrovaní uživatelé a jejich hesla
users = {"bob":"123", "ann":"pass123", "mike":"password123", "liz":"pass123"} 

# Počet pomlček jako oddelovace
separator = "-" * 50 

# Přihlášení.
login = input("Enter your login: ").lower()
password = input("Enter your password: ")


if login in users.keys() and users[login] == password:
    # Přihlašovací údaje jsou správné.
    print(separator, f"Welcome to the app, {login}", "We have 3 texts to be analyzed.", separator, sep = "\n")   
else:
      # Přihlašovací údaje jsou špatné.
    print("Unregistered user, terminating the program..!")
    quit()

# Výběr textu k analýze
text_num = input("Enter a number (integer) btw. 1 and 3 to select: ") 

if not text_num.isdigit():
    print("You did not select an integer, terminating the program..!")
    quit()
elif int(text_num) <1 or int(text_num) >3:
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

# Počet slov začínající velkým písmenem ve vybraném textu
titlecase = []
for title_word in clear_words:
    if  title_word != title_word.lower() and title_word.isalpha():      # Nebere v potaz čísla v textu
        titlecase.append(title_word)  # Přidej ji do seznamu slov s velkým písmenem na začátku"

print(f"There are {len(titlecase)} titlecase words.")

# Počet slov psaných velkým písmenem ve vybraném textu
uppercase = []
for upper_word in clear_words:
    if upper_word.isalpha() and upper_word.isupper():      # Nebere v potaz čísla v textu
        uppercase.append(upper_word)  # Přidej ji do seznamu slov psaných velkým písmenem"
print(f"There are {len(uppercase)} uppercase words.")


# Počet slov psaných malým písmenem ve vybraném textu
lowercase = []
for lower_word in clear_words:
    if lower_word.isalpha() and lower_word.islower():      # Nebere v potaz čísla v textu 
        lowercase.append(lower_word)  # Přidej ji do seznamu slov psaných malým písmenem"
print(f"There are {len(lowercase)} lowercase words.")

# Počet čísel ve vybraném textu
numbers = []
for number in clear_words:
    if number.isdigit():       
        numbers.append(int(number))  # Přidej ho do seznamu čísel"
print(f"There are {len(numbers)} numeric strings.")
print(f"The sum of all the numbers: {sum(numbers)}")

# Data pro graf
words_length={}
for length in clear_words:
    if len(length) not in words_length:
        words_length[len(length)] = 1
    else:
        words_length[len(length)] += 1

max_range = int(max(words_length.keys())) + 1

# Graf
print (separator, "LEN".rjust(5) + "|   OCCURENCES   |NR.", separator, sep="\n")

for key in range(1,max_range):
    space = 16 - words_length[key]
    print(str(key).rjust(5), "|", "*" * words_length[key], " " * space, "|", words_length[key], sep="")
print(separator)

