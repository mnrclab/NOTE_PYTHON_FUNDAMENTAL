#DICTIONARY

andi = {
    'name': 'Andi',
    'age': 22,
    'is_married': False,
    'job': 'PNS',
    'cars': ['Alphard', 'Xpander', 'Innova'],
    'address': {
        'street': 'Mawar Ungu',
        'RT': 5, 'RW': 121, 'kecamatan': 'X',
        'zipcode': 123456,
        'geo': {
            'lat': 111.111,
            'lng': 65.8370
        }
    }

}

print(andi['name'])
print(andi['age'])
print(andi['is_married'])

print(andi.get('name'))
print(andi.get('age'))
print(andi.get('is_married'))

print(andi.get('job', 'Maaf Andi masih nganggur')) #tidak error, dan tetap akan menampilkan, akan lebih bagus jika dideklar kalau tidak ada
#print(andi['job']) #kalau tidak ada di dictionary, maka akan muncul error
print(andi) #akan memunculkan seluruh data di dictionary
print(type(andi)) #mengecek data type of andi


andi['name'] = 'Budi' #mengubah value name dari Andi menjadi Budi
print(andi['cars'][0])
print(andi['address']['geo'])

'''
andi['salary'] = 25000000 #menambahkan data salary
andi.update({'no_ktp': 1234567891213232}) #menambahkan data no.ktp
print(list(andi)) #untuk mengubah ke dalam list
print(list(andi.keys())) #untuk melihat keys atau atributnya
print(list(andi.values())) #untuk melihat values
'''

days = {
    'senin': 'monday', 'selasa': 'tuesday', 'rabu': 'wednesday',
    'kamis': 'thursday', 'jumat': 'friday', 'sabtu': "saturday",
    'minggu': 'sunday'
}

hari = list(days)
day = list(days.values())

x = input('Ketik nama hari (ENG/IDN): ')

if x.lower() in hari:
    engHari = day[hari.index(x.lower())]
    print(f'Bhs Inggris {x.lower()} adalah {engHari}')
else:
    idDay = hari[day.index(x.lower())]
    print(f'Bhs Indonesia {x.lower()} adalah {idDay}')

#translator nama hari id = eng
hari = input('Ketik nama hari: ').lower()
hari_terj = days.get(hari, "Tidak ada")
print(f'Terjemahan nama hari {hari.upper()} adalah {hari_terj.upper()}')