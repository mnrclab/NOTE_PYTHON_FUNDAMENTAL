nama = 'Purwadhika Startup & Coding School'

#menghitung jumlah huruf tanpa spasi
print(len(nama.replace(' ', '')))

#menghitung jumlah huruf dan spasi
print(len(nama))

#jumlah huruf c ?
cari = 'c'
x = nama.upper().replace(cari.upper(), '')
print(x)
jmlCari = len(nama) - len(x)
print(f'Jumlah huruf \'{cari}\' ada = {jmlCari}')

#jumlah kata 'startup'
cari = 'startup'
x = nama.upper().replace(cari.upper(), '')
print(x)
jmlCari = int((len(nama) - len(x)) / len(cari))
print(f'Jumlah kata \'{cari}\' ada = {jmlCari}')