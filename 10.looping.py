#FOR LOOPS

kota = ['Jakarta', 'Bandung', 'Surabaya']

i = 0
while i < len(kota):
    print(kota[i])
    i+= 1

for i in range(len(kota)):
    print(kota[i])

for namaKota in kota:
    print(namaKota)

x = 'purwadhika'
for i in x:
    print(i)

for i in range(10, 50, 8):
    print(i)
else:
    print('OK')

for i in range(2, 10):
    print(i)
    if i == 7:
        break #akan berhenti ketika i di angka 7


for i in range(2, 10):
    if i == 7:
        break #akan berhenti ketika i di angka 7, tapi angka 7 tidak ter-print
    print(i)

for i in range(2, 10):
    if i == 7:
        continue #pengulangan akan skip di angka 7, lalu lanjut 8 dst.
    print(i)

for i in range(1, 11):
    if i % 2 == 0:
        print('WOW')
    else:
        print(i)


#program untuk membalikkan urutan list
x = [1, 2, 3, 5, 6, 7, 8, 9, 10]
y = ['Andi', 'Budi', 'Caca']


x_balik = []
for i in range(1, len(x)+1):
    x_balik.append(x[-i])
print(x_balik)

def balikPosisi(mylist):
    hasil = []
    for i in range(len(mylist)):
        hasil.insert(0, mylist[1])
    return hasil

print(balikPosisi(x))

def BalikPosisi(mylist):
    for e in range(round(len(mylist)/2)):
        asli = mylist[e]
        mylist[e] = mylist[len(mylist)-1-e]
        mylist[len(mylist)-1-e] = asli
    return mylist

print(BalikPosisi(x))
print(BalikPosisi(y))



#CARA PERTAMA
x.reverse()
print(x)

#CARA KEDUA
print(x[::-1])

#CARA KETIGA
print(list(reversed(x)))

#SEGITIGA SIKU-SIKU

star = ''
for i in range(10):
    star += ' * '
    print(star)

def star(x):
    star = ''
    for i in range(x):
        star += ' * '
        print(star)
    return i

# SEGITIGA SIKU-SIKU TERBALIK

# cara pertama
star = int(input('Berapa banyak bintang?: '))
z = ''
for x in range(0, star):
    for y in range (0, star-x):
        z += '*'
    z += '\n'
print(z)

# cara kedua
def rStar(x):
    star = ''
    for i in range(x):
        star = ' * ' * (x-1)
        print(star)

# rStar(10)
def pangkat(x, y):
    out = 1
    for i in range(y):
        out *= x
    print(out)
pangkat(2,2)