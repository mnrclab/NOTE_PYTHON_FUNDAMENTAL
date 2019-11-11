# TUPLE

x = [
    (1, ['a', 'b', 'c'], 3),
    (4, 5, 6)
]
x[0][1][2] = 'Andi'
x[0][1].append('d')

x = tuple(x)
x[0][1][2] = 'Budi'
x[0][0] = 'Caca' #tidak bisa karena dalam tuple
print(x)


# set/himpunan
# 1. no indexing
# 2. duplicate elements not allowed
# 3. set adalah variabel, tapi variabelnya harus elemen immutable

z = {1, 2, 3, 1, 2, 3}
z.add('a') #menambah karakter a
z.add(('c', 'd', 'e'))
print(z)
z.add([9, 8, 7]) #tidak bisa karena list adalah mutable
print(z)

MENGEDIT VARIABEL SET.

# CARA PERTAMA
z = list(z)

# CARA KEDUA
a = []
for i in z:
    a.append(i)
print(a)

z = {1, 2, 3, 1, 2, 3}
z.add('andi')
z.update([6, 7, 8])
z.update({6, 'budi', 'andi'})

z.remove('budi') #menghapus elemen
z.discard('andi') #menghapus elemen, tapi bisa file yang tidak ada
print(z)
z.pop() #menghapus elemen terakhir
z.clear() #menghapus seluruh elemen
del z #menghapus eksistensi variabel z
print(z)