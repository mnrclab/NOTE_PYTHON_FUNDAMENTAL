# IF

x = 5

#equation
print(x == 4)
print(x >= 4)
print(x <= 4)

#comparison
print(x > 4)
print(x < 4)
print(x != 4)

#SOAL PERTAMA
nilai = int(input('Masukkan nilai Anda:'))

if(nilai>95) :
    print('Alhamdulillah')
elif(nilai >= 70 and nilai <=100):
    print('Lulus')
else:
    print('Hindari ya')


#SOAL KEDUA
jomblo = True

if(jomblo):
    print('Masih available')
else:
    print('Sold out')

jomblo = False; nganggur = True

if jomblo and nganggur:
    print('Anda jomblo pengangguran')
elif jomblo and not nganggur:
    print('Anda kurang piknik')
elif not jomblo and nganggur:
    print('Anda eceng gondok')
else:
    print('Anda OK')

# SOAL
nilai = 98

if (nilai >= 82):
    print('nilai Anda adalah A')
elif (nilai >=72 and nilai <=81):
    print('nilai Anda adalah B')
elif (nilai >= 62 and nilai <=71):
    print('nilai Anda adalah C')
elif (nilai >= 52 and nilai <= 61):
    print('nilai Anda adalah D')
else:
    print('Nilai Anda adalah E')