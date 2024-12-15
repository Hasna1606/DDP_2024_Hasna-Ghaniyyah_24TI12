from animal import Animal 

class Bird(Animal):
    #Konstruktor Properti
    def __init__(self, nama, makanan, hidup, berkembangBiak, warna, paruh):
        super().__init__(nama, makanan, hidup, berkembangBiak)
        self.warna = warna
        self.paruh = paruh

    #Method
    def infoBird(self):
        super().infoAnimal()
        print('Warna\t\t\t: ', self.warna, '\nJenis Paruh\t\t: ', self.paruh)

#Objek
print('---Info Bird---')
bird = Bird('Burung Elang', "Biji", "Pohon", "Bertelur", "Coklat", "Bengkok dan Lancip\n")
bird.infoBird()
bird = Bird('Burung Hantu', "Daging", "Hutan", "Bertelur", "Coklat", "Pendek, melengkung, dan menghadap ke bawah dengan ujungnya yang bengkok\n")
bird.infoBird()
bird = Bird('Burung Kakak Tua', "Biji", "Hutan Bakau", "Bertelur", "Putih", "Pendek, bengkok dan tajam")
bird.infoBird()