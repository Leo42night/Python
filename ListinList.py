# 3. Seorang dosen ingin data-data nilai mahasiswanya dihitung dan dibuatkan programnya. 
# Gunakan list untuk membuat program yang mempunyai ketentuan sebagai berikut : 
	# a. Nama mahasiswa, nilai tugas, nilai UTS dan nilai UAS di input. 
	# b. Proses yang dilakukan untuk mendapatkan nilai murni dari masing masing nilai adalah : 
		# ▪ Nilai murni tugas = nilai tugas x 30% 
		# ▪ Nilai murni UTS = nilai UTS x 30% 
		# ▪ Nilai UAS = nilai UAS x 40% 
		# ▪ Nilai akhir = Nilai murni tugas + Nilai murni UTS + Nilai murni UAS 
	# c. Ketentuan untuk grade nilai : 
		# ▪ Nilai akhir >=80 mendapat grade A 
		# ▪ Nilai akhir >=70 mendapat grade B 
		# ▪ Nilai akhir >=59 mendapat grade C 
		# ▪ Nilai akhir >=50 mendapat grade D 
		# ▪ Nilai akhir <50 mendapat grade E
all_list=[]
jmah=int(input("masukkan jumlah mahasiswa : "))
for i in range(jmah):
	mah=input("masukkan nama mahasiswa : ")
	n_tugas=int(input("nilai tugas : "))
	n_murt=n_tugas*3/10 #nilai murni tugas
	n_uts=int(input("nilai UTS : "))
	n_muruts=n_uts*3/10 #nilai murni UTS
	n_uas=int(input("nilai Uas : "))
	n_muruas=n_uas*4/10 #nilai murni UAS
	n_akh=n_murt+n_uts+n_muruas #nilai Akhir
	c=[mah,n_murt,n_muruts,n_muruas,n_akh] #kelompokkan value print
	if n_akh <5 :
		c.append("E")
	elif n_akh >=5 :
		c.append("D")
	elif n_akh >=6 :
		c.append("C")
	elif n_akh >=7 :
		c.append("B")
	elif n_akh >=8 :
		c.append("A")
	d=str(c) #ubah list c menjadi string d
	all_list.append(d) #setiap str d menjadi data dalam list[]all_list
e='\n'.join(all_list) #semua data list bergabung dalam e, dan terspasi antar index str
print("jumlah mahasiswa : ",jmah)
print ("['nama mahasiswa', NMTugas, NMUts, NMUas, NAkhir, 'Grade']")
print (e)