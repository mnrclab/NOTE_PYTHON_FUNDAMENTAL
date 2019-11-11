# FUNCTION

def namaFunction():
    program;
# =========================================

def hello():
    print('Hello World!')

hello(); hello(); hello()

# #membuat fungsi f(x) = x ^ 2
def kuadrat(angka):
    print(angka**2)
print(kuadrat(2))

# #membuat fungsi f(x) = x ^ 2

def pangkat(angka1, angka2): #dua parameter
    print(angka1 ** angka2)

pangkat(2, 1)
pangkat(2, 15)

# LATIHAN DI KELAS

# membuat fungsi kalkulator

def kalkulator():
    angka1 = float(input('Masukkan angka 1: '))
    operator = input('Masukkan operator aritmatika (+-*/): ')
    angka2 = float(input('Masukkan angka 2: '))
    if operator == '+':
        print(f'Hasil penghitungannya yaitu {angka1 + angka2}')
    elif operator == '-':
        print(f'Hasil penghitungannya yaitu {angka1 - angka2}')
    elif operator == '*':
        print(f'Hasil penghitungannya yaitu {angka1 * angka2}')
    elif operator == '/':
        print(f'Hasil penghitungannya yaitu {angka1 / angka2}')
    else:
        print(f'Maaf operator {operator} tidak dikenali')

kalkulator()

# =========================================

students = ['Andi', 'Budi', 'Caca']

def tes(students):
    print(students[0])
    print('Caca' in students)

tes(students)

# =========================================

def LuasPersegi(sisi):
    print('Luas =', sisi * sisi)
def LuasPersegiReturn(sisi):
    return sisi * sisi # fungsi yang bisa diprint setiap waktu dan mengandung value (sisi * sisi)

LuasPersegi(4) #mengambil fungsi awal
print(LuasPersegiReturn(5)) #memanggil fungsi return


# =========================================

# WHILE LOOP
'menu pengulangan untuk menjalankan suatu perintah yang berulang'

i = 1
while i <= 20:
    print(i)
    i += 1

i = 20
while i >= 1:
    print(i)
    i -= 2

# =========================================
students = ['Andi', 'Budi', 'Caca', 'Deni']
index = 0
while index <= len(students) - 1:
    print(students[index])
    index += 1

# =========================================
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = []
index = 0
while index <= len(x)-1:
    y.append(x[index] ** 2)
    index += 1
print(y)

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = []
index = 0
while index <= len(x)-1:
    if index == 4:
        break
    y.append(x[index] ** 2)
    index += 1
print(y)
# =========================================
i = 0
while i < 10:
    i += 1
    if i == 5:
        continue
    print(i)


