# SOAL AYAH & ANDI

total_umur = 50
rasio_UmurAndi = 1
rasio_UmurAyah = 6
total_rasio = rasio_UmurAndi + rasio_UmurAyah
tambahan_waktu = 4


UmurAndi = ((total_umur-tambahan_waktu) + (rasio_UmurAyah * tambahan_waktu))/ total_rasio
print('Umur Andi Sekarang: ', round(UmurAndi))

UmurAyah = total_umur - UmurAndi

print('Umur Ayah Sekarang: ', round(UmurAyah))

# SOAL IBU & ANAK

rasio_dulu = 1/4
tambahan_rasio_dulu = 1/2
rasio_sekarang = 1/7
tambahan_rasio_skrng = 19

UmurIbu = (rasio_dulu * tambahan_rasio_skrng + tambahan_rasio_dulu) / (rasio_dulu - rasio_sekarang )
print('Usia Ibu Sekarang: ', round(UmurIbu))

UmurAnak = rasio_sekarang * UmurIbu + tambahan_rasio_skrng
print('Usia Anak Sekarang: ', round(UmurAnak))

UmurMelahirkan = UmurIbu - UmurAnak
print('Usia Ibu Melahirkan: ', round(UmurMelahirkan))