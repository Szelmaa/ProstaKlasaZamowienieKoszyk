class Zamowienie:
    def __init__(self, koszyk, klient):
        self.koszyk = list(koszyk)
        self.klient = klient

    def __len__(self):
        return len(self.koszyk)

    def __add__(self, artykul):
        nowy_koszyk = self.koszyk.copy()
        nowy_koszyk.append(artykul)
        return Zamowienie(nowy_koszyk, self.klient)


zamowienie = Zamowienie(['mydło', 'kawa', 'cukier'], 'Jan Kowalski')
print(len(zamowienie))

zamowienie = zamowienie + 'czekolada' + 'jogurt'
print(zamowienie.koszyk)
print(len(zamowienie))
