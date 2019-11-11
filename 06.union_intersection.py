a = list('abcde')
b = list('bcdfgh')

# A intersection pada B

a= set(a)
b= set(b)

#intersection/ yang dimiliki oleh himpunan A dan B
print(a.intersection(b))
print(b.intersection(a))
print(a & b)
print(a & b)

#union/menggabungkan seluruh anggota himpunan A dan B
print(a.union(b))
print(b.union(a))
print(a | b)
print(a | b)

#selisih/anggota khusus yang hanya dimiliki satu himpunan/difference
print(a.difference(b))
print(b.difference(a))
print(a - b)
print(b - a)

#symmetric diff/beda setangkup/yang hanya dimiliki oleh A plus B
print(a.symmetric_difference(b))
print(b.symmetric_difference(a))
print(a ^ b)
print(b ^ a)

# SOAL 
p = [1,2,4,7,9,19]
q = [5,12,16,17,7,9,19,6]
r = [19, 6, 3, 8]

P = set(p)
Q = set(q)
R = set(r)

print(P & Q)
print(P & Q & R)
print(P - Q - R)