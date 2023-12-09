print("Cześć, powodzenia w quizie! Zaczynajmy")

#pytanie 1
print("Jakim skrótem oznaczona jest liczba całkowita?") 
odpowiedzi1=["float","int","str"]
print(odpowiedzi1)

while True:
    odpowiedz = input("Podaj odpowiedź: ")
    
    if odpowiedz == "int":
        print("Odpowiedź poprawna!")
        break  # Zakończ pętlę, jeśli odpowiedź jest poprawna
    else:
        print("Odpowiedź nieprawidłowa. Spróbuj jeszcze raz.")

#pytanie 2
print("Jak nazywa się pętla, która będzie trwać nieskończoność?")
odpowiedzi2=["for","while"]
print(odpowiedzi2)

while True:
    odpowiedz = input("Podaj odpowiedź: ")
    
    if odpowiedz == "while":
        print("Odpowiedź poprawna!")
        break  # Zakończ pętlę, jeśli odpowiedź jest poprawna
    else:
        print("Odpowiedź nieprawidłowa. Spróbuj jeszcze raz.")

#pytanie 3
print("Co oznacza komenda if?")
odpowiedzi3=["w przeciwnym razie","napisz","jeżeli"]
print(odpowiedzi3)

while True:
    odpowiedz = input("Podaj odpowiedź: ")
    
    if odpowiedz == "jeżeli":
        print("Odpowiedź poprawna!")
        break  # Zakończ pętlę, jeśli odpowiedź jest poprawna
    else:
        print("Odpowiedź nieprawidłowa. Spróbuj jeszcze raz.")

#pytanie 4
print("Jaką komendą usuwamy element z listy?")
odpowiedzi4=["remove","sort","insert"]
print(odpowiedzi4)

while True:
    odpowiedz = input("Podaj odpowiedź: ")
    
    if odpowiedz == "remove":
        print("Odpowiedź poprawna!")
        break  # Zakończ pętlę, jeśli odpowiedź jest poprawna
    else:
        print("Odpowiedź nieprawidłowa. Spróbuj jeszcze raz.")

print("Bardzo dobrze ci poszło! Dziękuję za wzięcie udziału w quizie!")