kot = "=^_^="
iloscKotów = input("Ile chcesz kotów ")
try:
    iloscKotów = int(nr_karty)
except ValueError as owcaError:
    print("Nie wpisałeś liczby ")
    nr_karty = 7

# zadanie domowe
"""
napiać program ktory generuje piramide z kotów
Założenia:
Jeśli użytkownik wpisze liczbę ujemną to powinno go okrzyczeć i napisać =^!^=
Przykład:
dla ilośćKotów = 3

Wynik:
=^_^=
=^_^==^_^=
=^_^==^_^==^_^=

hint:
Pętle for i if'y
"""