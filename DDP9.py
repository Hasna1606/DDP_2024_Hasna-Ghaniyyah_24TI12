#pendeklarasian fungsi hanya satu kali
def hello():
    print("hello ini adalah fungsi hello")
    print("selamat datang di nurul fikri")

#panggil fungsi bisa berkali-kali
hello()
hello() 

def cetak(kata) :
    print(kata)

cetak("hallo")

def biodata(nama = "Bagas", alamat = "Jakarta", umur = 17) : #Function default
    cetak("nama saya adalah" + nama)
    cetak("alamat saya" + alamat)
    cetak("umur saya berusia" + str(umur))

biodata("Hasna", "Bogor", 18)
biodata("Zahra", "Depok") #harus diisi sama 
biodata()

def perkalian(a, b):
    print(a*b)

perkalian(3,4) #12
perkalian(10, 10) #100

def luas_persegi(sisi):
    print(sisi*sisi)
luas_persegi(10)

def bilangan1(x):
    return x*4
    
def bilangan2(y):
    return y*y

cetak(bilangan1(2) + bilangan2(3))
