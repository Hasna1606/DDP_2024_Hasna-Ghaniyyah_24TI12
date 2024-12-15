from animal import Animal

class Fish(Animal):
    #Konstruktor Properti
    def __init__(self, nama, makanan, hidup, berkembangBiak, pernapasan, habitat):
        super().__init__(nama, makanan, hidup, berkembangBiak)
        self.pernapasan = pernapasan
        self.habitat = habitat

    #Method
    def infoFish(self):
        super().infoAnimal()
        print('Jenis Bernapas\t\t: ', self.pernapasan, '\nHabitat\t\t\t: ', self.habitat)

#Objek
print('---Info Fish---')
fish = Fish('Ikan Hiu', "Daging", "Laut", "Melahirkan", "Insang", "Air Asin\n")
fish.infoFish()
fish = Fish('Ikan Paus', "Daging", "Samudra", "Melahirkan", "Paru-paru", "Perairan Tropis\n")
fish.infoFish()
fish = Fish('Ikan Lumba-lumba', "Daging", "Laut", "Melahirkan", "Paru-paru", "Air Tawar")
fish.infoFish()

