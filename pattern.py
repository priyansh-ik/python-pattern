a=input('Enter 1st word : ')

b=input('Enter 2nd word : ')

n=len (a)

w=len (b)

if n>w:
	print(b)
	q=(n//2)
	g=n-1
	s=g-2
	f=(n//2)-1
	print(a[:1], (g)*'\t', a[ (n-1):])
	for i in range (1,f+1):
		if s>1:
			print(i*'\t',a[(-n+i):(-n+(i-1)):-1],s*'\t',a[ - (i+1) : -i])
		elif s==1:
			print(i*'\t',a[(-n+i):(-n+(i-1)):-1], '\t', a[-(i+1):-i])
		s= (s) - 2
	if n%2==1:
		print(q*'\t', a[q])
else:
	print(a)
	q=(w//2)
	g=w-1
	s=g-2
	f=(w//2)-1
	print (b[:1], (g)*'\t',b[(w-1):])
	for i in range (1, f+1) :
		if s>1:
			print(i*'\t',b[(-w+i): (-w+(i-1)):-1], s*' \t',b[-(i+1):-i])
		elif s==1:
			print(i*'\t',b[(-w+i): (-w+(i-1)):-1], '\t',b[-(i+1):-i])
		s= (s) - 2
	if w%2==1:
		print(q*'\t',b[q])