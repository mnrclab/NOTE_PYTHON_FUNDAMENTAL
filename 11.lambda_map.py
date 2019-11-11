
def pangkatB(x, y):
    if(y == 1):
        return x
    else:
        return x * pangkatB(x, y-1)
print(pangkatB(2,3))


#rekursif fungsi

pangkatB(2,3) = 2 * pangkatB(2, 2)
pangkatB(2,2) = 2 * pangkatB(2, 1)
pangkatB(2,1) = 2 


# FACTORIAL

def factorial(x):
    if(x==0):
        return x+1
    elif(x==1):
        return x
    else:
        return x * factorial(x-1)
print(factorial(3))


# LAMBDA FUNCTION
x = lambda a,b,c : a+b+c
def y(a, b, c):
    return a+b+c

print(x(2,3,4))
print(y(2,3,4))
#=================================================================
def myFunction(x):
    return lambda a : a ** x #membuat sebuah function yang custom
pangkat2 = myFunction(2)
pangkat3 = myFunction(3)
print(pangkat3(2))
'''FLOW: nilai x akan diolah dengan a (sesuai operasi yang dimasukkan), 
lalu hasilnya bisa diolah lagi menjadi sebuah function dengan memanfaatkan fungsi (lambda) 
yang sudah dibuat.'''

# menguji apakah data ini adalah angka genap
x = lambda a : True if a % 2 == 0 else False
print(x(4))

def y(a):
    if a % 2 ==0:
        return True
    else:
        return False

x = lambda a : 'Angka Genap' if a % 2 == 0 else 'Angka Ganjil'
print(x(4))

x = lambda a : print(a)
x('Selamat Pagi') #akan menjalankan fungsi x yaitu print


# MAP PYTHON
def y(a):
    return len(a)
a = ['AndiSujatmika', 'Budi', 'Caca']

x = map(y, a)
print(x)
print(list(x)) 

a = ['Cokelat', 'Melon', 'Nangka']
b = ['Apel', 'Jeruk', 'Nanas']
def combi(a, b):
    return a+' '+b
x = map(combi, a, b)
print(x)
print(list(x))

x = [2, 4, 6, 8, 10]
def pangkat2(x):
    return x**2
y = map(pangkat2, x)
print(y)
print(list(y))

z = map(lambda a:a**2, x)
print(list(z))

b = []
for i in x:
    b.append(i ** 2)
print(i)

x = range(11)
print(list(x))

#=================================================================
def diatasLima(x):
    if x < 5:
        return False
    else:
        return True
y = filter(diatasLima, x) #akan mem-filter atau mencari yang True saja.
print(list(y))

z = filter(lambda a: True if a >= 5 else False, x)
print(list(z))

x = pow(2, 2)
y = pow(3, 3)
print(x)
print(y)

z = list(map(pow, [2,3], [2,3]))
print(z)

x = [1, 2, 3, 4, 5, 99]
y = [1, 2, 5, 8, 7, 99]
z = list(filter(lambda a: a in x, y)) #membuat variabel z, yang isinya adalah fungsi filter untuk mencari data yang ada di x dan y
print(z)
#=================================================================
# FUNGSI REDUCE
angka = [1, 2, 3, 4]
# 1 x 2 x 3 x 4 = 24

hasil = 1
for i in angka:
    hasil *= i
print(hasil)
#=================================================================
from functools import reduce
z = reduce(lambda x,y: x / y, angka) #menyatukan (reduce) elemen-elemen yang ada dalam data angka, dengan cara perkalian (sesuai permintaan)
print(z)

kata = ['Andi', 'Budi', 'Ayah']

print(''.join(kata))

from functools import reduce
z = reduce(lambda x,y: x+y, kata)
print(z)
#=================================================================
# FILTER() IN MAP()

angka = [1, 2, 3, 4]

z = list(map(lambda x : x * 2, filter(lambda x: x>3, angka)))
print(z)

z = list(filter(lambda x: x>3, map(lambda x : x * 2, angka)))
print(z)
#=================================================================
# nomor = [1 - 100], setiap angka genap dikali 2
# semua angka hasilnya dikalihkan satu sama lain

from functools import reduce
angka = range(101)

z = reduce(lambda x,y: x + y, list(map(lambda x: x * 2, list(filter(lambda x: x % 2 == 0, angka)))))
print(z)

v = list(filter(lambda x: x%5 or x==5, filter(lambda x: x%3 or x==3, filter(lambda x: x%2 or x==2, filter(lambda x: x>1, angka)))))
print(v)

v = list(filter(lambda x: (x%5 or x==5) and (x%3 or x==3) and (x%2 or x==2) and (x>1), angka))
print(v)
#=================================================================
def prima(x):
    a = False
    if x > 1:
        if x == 2: a = True
        else:
            for i in range(2, x):
                if x % i == 0: return False; break
                else: a = True
    else: a = False
    return a
print(prima(81))

#=================================================================
x = lambda a : 'Angka Genap' if a % 2 == 0 else 'Angka Ganjil'

angka = int(input('Masukkan angka yang ingin dites: '))
y = lambda a : 'Bilangan Prima' if (a == 2) or (angka % a == 0) else 'Bukan Bilangan Prima'
print(y(angka))
