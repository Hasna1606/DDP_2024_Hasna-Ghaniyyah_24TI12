import math

#luas permukaan bangun ruang kubus
def luasPermukaanKubus(sisi):
    return 6 * sisi * sisi

#luas permukaan bangun ruang balok 
def luasPermukaanBalok(panjang,tinggi,lebar):
    return 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
   
#luas permukaan bangun ruang tabung
def luasPermukaanTabung(r,tinggi):
    return 2 * math.pi * r * (r + tinggi)

#luas permukaan bangun ruang limas
def luasPermukaanLimas(luasAlas, luasSisiTegak):
    return luasAlas + luasSisiTegak

#luas permukaan bangun ruang prisma
def luasPermukaanPrisma(luasAlas, kelilingAlas, tinggi):
    return 2 * luasAlas + kelilingAlas * tinggi