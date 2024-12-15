class Animal:
    #konstruktor
    def __init__(self, nama, makanan, hidup, berkembangBiak):
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembangBiak = berkembangBiak

    #method informasi
    def infoAnimal(self):
        print('Nama Hewan\t\t: ', self.nama, '\nMakanan\t\t\t: ', self.makanan, '\nHidup\t\t\t: ', self.hidup, '\nBerkembang Biak\t\t: ', self.berkembangBiak)
    


    