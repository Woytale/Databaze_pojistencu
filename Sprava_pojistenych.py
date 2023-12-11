class Pojisteny: #obsahuje informace o pojištěné osobě: jméno, příjmení, věk a telefonní číslo
    def __init__(self, jmeno, prijmeni, vek, telefon):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon = telefon

    def __str__(self): #vrací informace o pojištěné osobě ve formátu řetězce
        return f"Jméno: {self.jmeno}, Příjmení: {self.prijmeni}, Věk: {self.vek}, Telefon: {self.telefon}"


class SpravaPojisteni: #obsahuje seznam pojištěných osob a několik metod pro manipulaci se seznamem
    def __init__(self):
        self.seznam_pojistenych = []

    def vytvor_pojisteneho(self, jmeno, prijmeni, vek, telefon): #vytváří nové instance třídy Pojisteny a přidává je do seznamu pojištěných
        if not jmeno:
            print("Chyba: Jméno nesmí být prázdné.")
            return
        pojisteny = Pojisteny(jmeno, prijmeni, vek, telefon)
        self.seznam_pojistenych.append(pojisteny)

    def zobraz_seznam_pojistenych(self): #vypisuje informace o všech pojištěných osobách uložených v seznamu
        if not self.seznam_pojistenych:
            print("Seznam pojištěných je prázdný.")
            return
        for pojisteny in self.seznam_pojistenych:
            print(pojisteny)

    def najdi_pojisteneho(self, jmeno, prijmeni): #vyhledá pojištěnou osobu podle zadaného jména a příjmení a vypíše informace o ní, pokud je nalezena
        nalezeno = False
        for pojisteny in self.seznam_pojistenych:
            if pojisteny.jmeno.lower() == jmeno.lower() and pojisteny.prijmeni.lower() == prijmeni.lower():
                print("Pojistěný nalezen:", pojisteny)
                nalezeno = True
                break
        if not nalezeno:
            print("Pojistěný s tímto jménem a příjmením nebyl nalezen.")

    def smaz_pojisteneho(self, index): #může smazat pojištěnou osobu ze seznamu na základě zadaného indexu
        if 0 <= index < len(self.seznam_pojistenych):
            del self.seznam_pojistenych[index]
            print("Pojištěný byl úspěšně smazán.")
        else:
            print("Neplatný index.")

    @staticmethod
    def match(pojisteny, jmeno, prijmeni): #kontrola zda zadaná osoba odpovídá jménu a příjmení ze seznamu
        return pojisteny.jmeno.lower() == jmeno.lower() and pojisteny.prijmeni.lower() == prijmeni.lower()

    # metody pro získání a nastavení seznamu pojištěných
    def get_seznam_pojistenych(self):
        return self.seznam_pojistenych

    def set_seznam_pojistenych(self, novy_seznam):
        self.seznam_pojistenych = novy_seznam



"""Funkce vytváří počáteční data pro správu pojištěných osob. Data obsahují informace o několika osobách, 
které jsou přidány do seznamu pojištěných pomocí metody vytvor_pojisteneho."""
def vytvor_pocatecni_data(sprava):
    data = [
        {"jmeno": "Josef", "prijmeni": "Novák", "vek": 35, "telefon": "333333333"},
        {"jmeno": "Jana", "prijmeni": "Váchová", "vek": 25, "telefon": "777777777"},
        {"jmeno": "Jan", "prijmeni": "Kovář", "vek": 45, "telefon": "666666666"},
        {"jmeno": "Miriam", "prijmeni": "Munzarová", "vek": 50, "telefon": "111111111"},
        {"jmeno": "Tomáš", "prijmeni": "Jedno", "vek": 30, "telefon": "222222222"},
    ]
    for osoba in data:
        sprava.vytvor_pojisteneho(osoba["jmeno"], osoba["prijmeni"], osoba["vek"], osoba["telefon"])



"""Main uživatele vyzývá k volbě různých akcí (zobrazení, vyhledání, smazání nebo přidání pojištěného) skrze klávesnici. 
Podle volby uživatele se volají odpovídající metody třídy SpravaPojisteni."""
def main():
    sprava = SpravaPojisteni()
    vytvor_pocatecni_data(sprava)

    while True:
        print("\nVyberte akci:")
        print("1. Zobrazit seznam pojištěných")
        print("2. Vyhledat pojištěného")
        print("3. Smazat pojištěného")
        print("4. Přidat nového pojištěného")
        print("5. Konec")

        volba = input()

        if volba == "1":
            sprava.zobraz_seznam_pojistenych()
        elif volba == "2":
            jmeno = input("Zadejte jméno pro vyhledání: ")
            prijmeni = input("Zadejte příjmení pro vyhledání: ")
            sprava.najdi_pojisteneho(jmeno, prijmeni)
        elif volba == "3":
            index = int(input("Zadejte index pojištěného pro smazání: "))
            sprava.smaz_pojisteneho(index)
        elif volba == "4":
            jmeno = input("Zadejte jméno: ")
            prijmeni = input("Zadejte příjmení: ")
            vek = int(input("Zadejte věk: "))
            telefon = input("Zadejte telefonní číslo: ")
            sprava.vytvor_pojisteneho(jmeno, prijmeni, vek, telefon)
            print("Nový pojištěný byl přidán.")
        elif volba == "5":
            print("Aplikace končí.")
            break
        else:
            print("Neplatná volba.")

if __name__ == "__main__":
    main()
