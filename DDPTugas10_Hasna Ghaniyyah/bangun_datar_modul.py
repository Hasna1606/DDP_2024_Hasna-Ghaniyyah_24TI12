import math
 
#luas bangun datar persegi
def luasPersegi(sisi):
    return sisi*sisi

#luas bangun datar segitiga
def luasSegitiga(alas,tinggi):
    return 1/2*alas*tinggi

#luas bangun datar lingkaran
def luasLingkaran(jari_jari):
    return math.pi*jari_jari**2

#luas bangun datar persegi panjang 
def luasPersegiPanjang(panjang,lebar):
    return panjang*lebar

#luas bangun datar jajar genjang
def luasJajarGenjang(alas, tinggi):
    return alas*tinggi