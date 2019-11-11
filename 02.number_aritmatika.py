x = 18
y = 2

print(x + y)
print(x - y)
print(float(x * y)) #untuk mengubah ke dalam float, angka koma
print(int(x / y)) #untuk mengubah ke dalam angka bulat/integer
print(float('1234.890'))
print(y ** 2) #untuk menghitung y pangkat 2
print(10 % 3) #untuk menghitung modulus, sisa 10 dibagi 3

x = -90.43432
print(abs(x))

print(pow(2, 3))
print(2 ** 3) #untuk mencari akar

# akar pangkat
print(4 ** (1/2))
print(27 ** (1/3))

print(max(1, 3, 4,5, 6, 7, 9 , 99, 0.1, 343, 33,.1, .8)) #mencari nilai maximal
print(min(1, 3, 4,5, 6, 7, 9 , 99, 0.1, 343, 33,.1, .8)) #mencari nilai minimal

print(round(356.97330343)) #pembulatan
print(round(356.97330343, 3)) #pembulatan 3 angka di belakang koma

print(0.1 + 0.2)

print(round((0.1 + 0.2), 1))

import math

print(math.pi) #mencari nilai akar
print(math.floor(3.9)) #pembulatan ke bawah
print(math.ceil(3.1)) #pembulatan ke atas
print(math.sqrt(196)) #mencari akar 196
print(math.factorial(3)) #mencari factorial, yaitu hasil 3 x 2 x 1


# JUMLAH AYAM & KAMBING
jml_hewan = 13
jml_kaki_hewan = 32
jml_kaki_ayam = 2
jml_kaki_kambing = 4
jml_sate_per_ayam = 50

jml_ayam = abs((jml_kaki_hewan-(jml_kaki_kambing*jml_hewan))/jml_kaki_ayam)
jumlah_sate = jml_ayam * jml_sate_per_ayam
print('jumlah ayamku:', jml_ayam)
print('jumlah sate ayam:', jumlah_sate)

jml_kambing = (jml_kaki_hewan - (jml_kaki_ayam*jml_ayam))/jml_kaki_kambing
print('jumlah kambingku:', jml_kambing)

# JUMLAH SAPI & KAMBING
jml_hewan = 13
jml_kaki_hewan = 32
jml_kaki_sapi = 4
jml_kaki_kambing = 4

jml_sapi = abs((jml_kaki_hewan-(jml_kaki_kambing*jml_hewan))/jml_kaki_sapi)
print('jumlah sapiku:', jml_sapi)

jml_kambing = (jml_kaki_hewan - (jml_kaki_sapi*jml_sapi))/jml_kaki_kambing
print('jumlah kambingku:', jml_kambing)

# MENGHITUNG USIA ANDI DAN BUDI
Andi = 2
Budi = 5
JU = 49
dua_tahun = 2

Usia_Andi = (Andi * (JU / (Andi + Budi))) + dua_tahun
print(Usia_Andi)

Usia_Budi = (Budi * (JU / (Andi + Budi))) + dua_tahun
print(Usia_Budi)


# WAKTU
import math

waktu = 485
tahun = 360
bulan = 30
minggu = 7

tahun_hitung = math.floor(waktu / tahun)

bulan_hitung = math.floor((waktu % tahun) / bulan)

print(tahun)


total_hewan = int(input('Ketik total hewan: '))
total_kaki_hewan = int(input('Ketik total kaki hewan: '))
total_kaki_A = int(input('Ketik total kaki hewan A: '))
total_kaki_B = int(input('Ketik total kaki hewan B: '))
hewan_A = abs((total_kaki_hewan-(total_kaki_A*total_hewan))/total_kaki_B)
hewan_B = (total_kaki_hewan - (total_kaki_A*hewan_A))/total_kaki_B
print(f'hewan A = {int(hewan_A)}, hewan B = {int(hewan_B)}')

total_hewan = int(input('Ketik total hewan: '))
total_kaki_hewan = int(input('Ketik total kaki hewan: '))
total_kaki_A = int(input('Ketik total kaki hewan A: '))
total_kaki_B = int(input('Ketik total kaki hewan B: '))
hewan_A = abs((total_kaki_hewan-(total_kaki_A*total_hewan))/total_kaki_B)
hewan_B = (total_kaki_hewan - (total_kaki_A*hewan_A))/total_kaki_B
print(f'hewan A = {int(hewan_A)}, hewan B = {int(hewan_B)}')


Waktu = 485
Tahun = 360
Bulan = 30
Minggu = 7

Wkt-Tahun = Waktu - Tahun
Wkt-Bulan = (Waktu - Tahun) / Bulan
Wkt-Minggu = ((Waktu - Tahun) - (Wkt-Bulan * Bulan)) / Minggu
Wkt-Hari = Waktu - (Wkt.)
