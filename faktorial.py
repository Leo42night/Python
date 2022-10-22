# Buatlah flowchart dan program untuk menghitung nilai faktorial Faktorial 
#(n) = n! = n x (n-1)! = n x (n-1) x (n-2) x … x (n-(n-1)) Misalnya: jika n=4, maka 4! = 4x3x2x1
aw=int(input("masukkan aw :"))
a=1
for i in range (aw):
	i+=1
	b=a*i
	a=b
	print(b)

