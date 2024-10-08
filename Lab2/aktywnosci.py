if __name__ == "__main__":
    czyKoniec = False
    
    aktywnosci = {}
    lacznyCzas = {}

    while not czyKoniec:
        print("Napisz 1 jeśli chcesz dodać aktywność, 2 jeśli chcesz pokazać czas, 3 jeśli chcesz pokazać top aktywności, 4 jeśli chcesz zakończyć")
        
        wybor = input()

        if wybor == "1":
            print("Podaj nazwę aktywności")
            nazwa = input()
            print("Podaj czas aktywności")
            czas = int(input())  
            if nazwa in aktywnosci:
                aktywnosci[nazwa].append(czas)  # Dodajemy czas do istniejącej listy
                lacznyCzas[nazwa] += czas       # Sumujemy czas
            else:
                aktywnosci[nazwa] = [czas]      # Tworzymy nową listę dla nowej aktywności
                lacznyCzas[nazwa] = czas        # Zapisujemy sumaryczny czas

        elif wybor == "2":
            print("Podaj nazwę aktywności")
            nazwa = input()
            if nazwa in lacznyCzas:
                print("Łączny czas: " + str(lacznyCzas[nazwa]))
            else:
                print("Aktywność o nazwie '" + nazwa + "' nie istnieje.")

        elif wybor == "3":
            print("Podaj ile aktywności chcesz zobaczyć")
            ile = int(input())  # Przekształcamy input na int
            print("Top " + str(ile) + " aktywności:")
            # Sortujemy słownik według wartości i zwracamy klucze
            top_aktywnosci = sorted(lacznyCzas, key=lacznyCzas.get, reverse=True)[:ile]
            for aktywnosc in top_aktywnosci:
                print(aktywnosc + ": " + str(lacznyCzas[aktywnosc]))

        elif wybor == "4":
            czyKoniec = True

        else:
            print("Niepoprawny wybór, spróbuj ponownie.")
