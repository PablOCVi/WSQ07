x=int(input("Ingresa desde que numero sumar: "))
y=int(input("Ingresa hasta que numero sumar: "))
z=x
while (z!=y):
	z=(z+1)
	c=(x+z)
	x=c
print("La suma es:",str(c))