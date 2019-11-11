X = 12
X = 13
X += 2 #melanjutkan X sebelumnya
X -= 2 #melanjutkan X sebelumnya
X *= 2 #melanjutkan X sebelumnya
X /= 2 #melanjutkan X sebelumnya
print(X)

x = 'abcdefghijklmnopqrstuvwqyz'
print(x[0:3]) #menampilkan karakter ke-0 sampe 3
print('r' in x) #membuktikan adanya karakter r dalam x, keluarnya angka boolean, True of False
print(x.count('g')) #menghitung karakter g dalam x

kalimat = "Hari ini Andi tidak kuliah"
cari = 'h'
print(cari.lower() in kalimat.lower()) #mencari nilai di variabel 'cari' dalam variabel 'kalimat'
print(kalimat.lower().count(cari.lower())) #menghitung karakter variabel cari dalam variabel kalimat, semuanya sudah dikecilkan

# ============================================
# VARIABEL LIST
# OPERATOR KURUNG SIKU []

x = ['Andi', 'Budi', 'Caca']
print(x)
print(type(x))
print(x[len(x) - 1])


#LIST
hari = ['senin', 'selasa', 'rabu', 'kamis', 'jum\'at', 'sabtu', 'minggu']

'''
Sekarang hari 'rabu', hari apakah 100 hari lagi?
'''
now = 'minggu'
brphari = 1
jml_hari = 7

sekarang = hari.index(now)
sisa_hari = brphari%jml_hari

hari_ke = hari[(sekarang+sisa_hari)%7]
print('hari masa depan adalah: ', hari_ke)


#LIST
hari = ['senin', 'selasa', 'rabu', 'kamis', 'jum\'at', 'sabtu', 'minggu']


# Sekarang hari 'rabu', hari apakah 100 hari yang lalu?

now = 'rabu'
brphari = -100
jml_hari = 7

sekarang = hari.index(now)
sisa_hari = brphari%jml_hari

hari_ke = hari[(sekarang+sisa_hari)%7]
print('prediksi hari:', hari_ke)

hari = ['senin', 'selasa', 'rabu', 'kamis', 'jum\'at', 'sabtu', 'minggu']

hari[0] = 'Monday'
hari.append('senin2') #memasukkan ke list, otomatis berada di terakhir
hari.insert(4, 'senin3') #memasukkan value senin3 di index ke-04
print(hari)

hari.remove('senin2') #menghapus elemen tertentu dalam list
hari.pop #menghapus elemen terakhir
hari.pop(4) #menghapus elemen ke-4
hari.clear #menghapus seluruh elemen dalam list
hari.sort() #mengurutkan elemen/konten baik angka atau huruf
hari.reverse() #mengurutkan terbalik dengan urutan berkebalikan urutan index
#pengurutan elemen tidak bisa dilakukan pada list yang berisi string dan integer
hari = hari[::-1] #mengurutkan terbalik dengan urutan berkebalikan urutan index
print(hari)


x = [1, 2, 3, 4, 5]
print(list(reversed(x))) #untuk mengubah menjadi list dan diurutkan secara terbalik

#MENG-COPY DATA
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = x.copy() #meng-copy seluruh data dari x
y = x[::2].copy() #meng-copy data dari x, yaitu start dari 0 sampai selesai, urutan/step ke-2 dan kelipatan

print(x)
print(y)
print(x+y) #menampilkan data x digabung data y
print(y * 2) #menampilkan data y sebanyak dua kali

# VARIABEL LIST DALAM LIST
z = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(z)
print(z[1][2]) #menampilkan elemen variabel z, list ke-1 dan list ke-2

a = [1, 2, 3] #ini list, dan bisa diubah elemennya, baik valuenya, edit, urutan
b = (1, 2, 3) #ini tuple, tidak bisa diedit dan dihapus, tapi bisa ditampilkan dua kali print(b*2)

print(tuple(a)) #mengubah list ke dalam tuple
print(list(b)) #mengubah tuple ke dalam list