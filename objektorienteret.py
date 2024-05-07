class Fag():

    def __init__(self, navnet, karakteren=None):
        self.navn = navnet
        self.karakter = karakteren

class KarakterBog():

    separator = '―'

    def __init__(self, elev='Navnløs'):
        self.elevNavn = elev
        self.data = []

    def tilføjFag(self, fag):
        self.data.append(fag)

    def beregnSnit(self):
        total = 0
        for fag in self.data:
            total += fag.karakter
        return 'Karaktergennemsnit af {} fag: {}\n'.format(len(self.data), round(total/len(self.data), 2))

    def genererKarakterOversigt(self):
        output = ''
        for fag in self.data:
            output += 'Karakteren i {} er: {}\n'.format(fag.navn.capitalize(), fag.karakter)
        return output

    def udskriv(self):
        print(self.separator * 35 + '\n')
        print('Karakterbog for:', self.elevNavn, '\n')
        print(self.beregnSnit())
        print(self.genererKarakterOversigt())
        print(self.separator * 35 + '\n')

martins = KarakterBog('Martin')
martins.tilføjFag(Fag('dansk', 4))
martins.tilføjFag(Fag('programmering', 12))
martins.tilføjFag(Fag('innovation', -3))
martins.tilføjFag(Fag('teknologi', -3))
martins.tilføjFag(Fag('opvask', 12))
martins.tilføjFag(Fag('racerbil', 12))

batmans = KarakterBog('Batman')
batmans.tilføjFag(Fag('sperlunking', 7))
batmans.tilføjFag(Fag('romancing', 2))
batmans.tilføjFag(Fag('public speaking', -3))
batmans.tilføjFag(Fag('ninja', 10))
batmans.tilføjFag(Fag('crime fighting', 12))
batmans.separator = '🦇'

batmans.udskriv()
martins.udskriv()
