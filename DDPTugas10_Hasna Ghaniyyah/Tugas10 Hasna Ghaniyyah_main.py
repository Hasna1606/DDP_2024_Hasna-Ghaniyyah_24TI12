from aritmatika_modul import * 
from bangun_datar_modul import *
from bangun_ruang_modul import *

def hitungan_aritmatika():
    print("\nPilih Operasi Aritmatika: ")
    print("1.Penjumlahan")
    print("2.Pengurangan")
    print("3.Perkalian")
    print("4.Pembagian")
    print("5.Pangkat")
    pilihan = int(input("\nMasukkan nomor operasi aritmatika yang dipilih (1-5): "))

    if pilihan == 1:
        a = float(input("Masukkan angka pertama: "))
        b = float(input("Masukkan angka kedua: "))
        print("Hasil Penjumlahan = ", tambah(a,b))

    elif pilihan == 2:
        a = float(input("Masukkan angka pertama: "))
        b = float(input("Masukkan angka kedua: "))
        print("Hasil Pengurangan = ", kurang(a,b))

    elif pilihan == 3:
        a = float(input("Masukkan angka pertama: "))
        b = float(input("Masukkan angka kedua: "))
        print("Hasil Perkalian = ", kali(a,b))

    elif pilihan == 4:
        a = float(input("Masukkan angka pertama: "))
        b = float(input("Masukkan angka kedua: "))
        print("Hasil Pembagian = ", bagi(a,b))

    elif pilihan == 5:
        a = float(input("Masukkan angka pertama: "))
        b = float(input("Masukkan angka kedua: "))
        print("Hasil Pangkat = ", pangkat(a,b))

    else :
        print("Pilihan tidak valid")

def luasBangunDatar():
    print("\nPilih Luas Bangun Datar: ")
    print("1. Luas Persegi")
    print("2. Luas Segitiga")
    print("3. Luas Lingkaran")
    print("4. Luas Persegi Panjang")
    print("5. Luas Trapesium")

    pilihan = int(input("\nMasukkan nomor luas bangun datar yang dipilih (1-5): "))

    if pilihan == 1:
        sisi = float(input("Masukkan nilai sisi: "))
        print("Hasil luas persegi = ", luasPersegi(sisi))

    elif pilihan == 2:
        alas = float(input("Masukkan nilai alas: "))
        tinggi = float(input("Masukkan nilai tinggi: "))
        print("Hasil luas segitiga = ", luasSegitiga(alas,tinggi))

    elif pilihan == 3:
        jari_jari = float(input("Masukkan nilai jari-jari: "))
        print("Hasil luas lingkaran = ", luasLingkaran(jari_jari))

    elif pilihan == 4:
        panjang = (input("Masukkan nilai panjang: "))
        lebar = float(input("Masukkan nilai lebar: "))
        print("Hasil luas persegi panjang = ", luasPersegiPanjang(panjang,lebar))

    elif pilihan == 5:
        alas = float(input("Masukkan alas: "))
        tinggi = float(input("Masukkan tinggi: "))
        print("Luas Jajar Genjang:", luasJajarGenjang(alas, tinggi))

    else:
        print("Pilihan tidak valid")

def luasBangunRuang():
    print("\nPilih Luas Permukaan Bangun Ruang: ")
    print("1. Luas Kubus")
    print("2. Luas Balok")
    print("3. Luas Tabung")
    print("4. Luas Limas")
    print("5. Luas Prisma")
    pilihan = int(input("\nMasukkan nomor luas permukaan bangun ruang yang dipilih (1-5): "))

    if pilihan == 1:
        sisi = float(input("Masukkan nilai sisi: "))
        print("Hasil luas permukaan kubus = ", luasPermukaanKubus(sisi))

    elif pilihan == 2:
        panjang = float(input("Masukkan nilai panjang: "))
        tinggi = float(input("masukkan nilai tinggi: "))
        lebar = float(input("Masukkan nilai lebar: "))
        print("Hasil luas permukaan balok = ", luasPermukaanBalok(panjang,tinggi,lebar))

    elif pilihan == 3:
        r = float(input("Masukkan nilai jari-jari: "))
        tinggi = float(input("Masukkan nilai tinggi: "))
        print("Hasil luas permukaan tabung = ", luasPermukaanTabung(r,tinggi))

    elif pilihan == 4:
        luasAlas = float(input("Masukkan nilai luas alas: "))
        luasSisiTegak = float(input("Masukkan nilai luas sisi tegak: "))
        print("Hasil luas permukaan limas = ", luasPermukaanLimas(luasAlas, luasSisiTegak))

    elif pilihan == 5:
        luasAlas = float(input("Masukkan nilai luas alas: "))
        kelilingAlas = float(input("Masukkan nilai keliling alas: "))
        tinggi = float(input("Masukkan nilai tinggi: "))
        print("Hasil luas permukaan limas = ", luasPermukaanPrisma(luasAlas, kelilingAlas, tinggi))

    else:
        print("Pilihan tidak valid")

def main():
    while True:
        print("\nPilih jenis perhitungan:")
        print("1. Operasi Aritmatika")
        print("2. Luas Bangun Datar")
        print("3. Luas Bangun Ruang")
        print("4. Keluar")
        
        pilihan = int(input("\nMasukkan pilihan (1-4): "))
        
        if pilihan == 1:
            hitungan_aritmatika()
        elif pilihan == 2:
            luasBangunDatar()
        elif pilihan == 3:
            luasBangunRuang()
        elif pilihan == 4:
            print("Terima kasih telah menggunakan program ini.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
