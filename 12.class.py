# CLASS = cetakan object
class Mobil:
    warna = 'merah'
    tahun = 2010

# create object mobil1
mobil1 = Mobil()
print(mobil1.tahun)
print(mobil1.warna)

class MobilCustom():
    def __init__(self, warna, tahun, model):
        self.color = warna
        self.year = tahun
        self.model = model

mobil1 = MobilCustom('pink', 2018, 'X')
mobil2 = MobilCustom('blue', 2010, ['A', 'B'])

print(mobil1.model)
print(mobil1.year)

# ===========================
class MobilCustom():
    def __init__(self, warna, tahun, model): #harus ada kata self untuk mengaktifkan initiation
        self.color = warna
        self.year = tahun
        self.model = model
    # method
    def jadul(self): #menambahkan function untuk mengecek kejadulan sebuah mobil
        if self.year < 2010:
            return True
        else: return False
    def tes(self):
        print(self.color, self.year, self.model, self.jadul())

mobilA = MobilCustom('merah', 1998, 'X')
mobilB = MobilCustom('merah', 2018, 'Z')

print(mobilA.year)
print(mobilA.jadul())
print(mobilA.tes())

# =========================================================
class Mobil:
    def __init__(self, warna, seat):
        self.warna = warna
        self.seat = seat

class Car(Mobil):
    pass #idem dengan data di atasnya / inheritance

mobil1 = Mobil('pink', 4)
car1 = Car('black', 8)
print(mobil1.warna, mobil1.seat)
print(car1.warna, car1.seat)

# =========================================================
class Mobil:
    def __init__(self, warna, seat):
        self.warna = warna
        self.seat = seat

class Car(Mobil):
    gps = True

mobil1 = Mobil('pink', 4)
car1 = Car('black', 8)
print(mobil1.warna, mobil1.seat)
print(car1.warna, car1.seat, car1.gps)

# =========================================================
class Mobil:
    def __init__(self, warna, seat):
        self.warna = warna
        self.seat = seat

class Car(Mobil):
    def __init__ (self, soundSys):
        self.soundSys = soundSys

mobil1 = Mobil(['pink', 'red'], 4)
car1 = Car(True)
print(mobil1.warna, mobil1.seat)
print(car1.soundSys)

# =========================================================
class X:
    def __init__(self, nama, gelar):
        self.nama = nama
        self.gelar = gelar

class Y(X):                             # cara pertama
    def __init__(self, nama, gelar):
        X.__init__(self, nama, gelar)

class Y(X):
    pass

class Y(X):
    def __init__(self, nama, gelar, univ):
        super().__init__(nama, gelar)
        self.kampus = univ

objX = X('Andi', "Prof.")
objY = Y('Budi', 'Dr.', 'UNPAD')
print(objX.nama)
print(objY.kampus)

# CARA MENAMPILKAN DATA YANG ADA DI DALAM CLASS

from pprint import pprint

pprint(vars(objY)) #menampilkan key secara urut
print(vars(objY))

print(objY.__dict__)

# CARA MENAMPILKAN VALUES
print(objY.nama)
print(getattr(objY, 'nama'))

# MENGECEK ATRIBUT/VALUES
print(hasattr(objY, 'warna'))
print(hasattr(objY, 'usia'))

# MENAMBAHKAN DATA
objY.warna = 'merah'
setattr(objX, 'alamat', 'BSD')

print(vars(objX))

# MENGHAPUS ATRIBUT
delattr(objX, 'alamat')
print(vars(objX))

#==========================================================
class Z:
    nama = 'Z'
    usia = 21

objZ = Z()
print(objZ.nama)
print(objZ.usia)

del Z.nama
print(objZ.usia)
print(objZ.nama) #sudah tidak ada

# ===========================================================

class student:
    def __init__(self, nama, usia):
        self.nama = nama
        self.usia = usia

data = [
        {'nama' : 'Andi', 'usia': 21},
        {'nama' : 'Budi', 'usia': 22},
        {'nama' : 'Caca', 'usia': 23},
        {'nama' : 'Deni', 'usia': 24},
]

def createObj(x):
    nama = x['nama']
    vars()[nama] = student(x['nama'], x['usia'])
    return vars()[nama]

def createObj(x):
    return student(x['nama'], x['usia'])

dataNew = list(map(
    lambda x: student(x['nama'], x['usia']), data
))

print(dataNew[0].nama)
print(dataNew[0].usia)

# ======================================================================
# MEMBUAT SEBUAH OBYEK 'PERSEGI' YANG DI DALAMNYA TERDAPAT FUNGSI MENGHITUNG KELILING DAN LUAS

class Persegi:
    def __init__(self, sisi):
        self.sisi = sisi
        self.keliling = self.sisi * 4
        self.luas = self.sisi ** 2

PersegiA = Persegi(4)
print(vars(PersegiA))
