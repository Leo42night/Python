angka=input("masukkan angka lewat spasi :")
urutAngka=angka.split()
#mulai listing
x=0 # x menyatakan mulai dari list pertama
while x < len(urutAngka):
	urutAngka[x]=int(urutAngka[x])
	x+=1
# sudah di list int
# lanjut mencari nilai terbesar
print(urutAngka)
i=0
y=0
while y != len(urutAngka): #bilangan ke-y di dalam urutAngka
	if i < urutAngka[y]: #dalam iteratif 
		i = urutAngka[y]
	y+=1 #iterasi bertambah
print (i)

