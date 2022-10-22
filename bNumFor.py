angka=input("masukkan angka lewat spasi :")
urutAngka=angka.split()
for i in range (len(urutAngka)):
	urutAngka[i]=int(urutAngka[i])

maxi = urutAngka[0]

for i in urutAngka :
	if i > maxi:
		maxi=i
print("bilangan terbesar adalah :",maxi)
