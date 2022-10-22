# angka jumlah dan rata-rata
print("menghitung jumlah dan rata-rata")
urutAngka = input("masukkan angka pisahkan dengan spasi : ")


# buat urutAngka menjadi list
angka = urutAngka.split()

# ubah item list menjadi tipe int
for i in range(len(angka)):
	angka[i]=int(angka[i])

# #hitung seluruh nilai jumlah dan rata-rata
print("jumlah =", sum(angka))
print("rata-rata =", sum(angka)/len(angka))