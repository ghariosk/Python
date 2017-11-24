def prime (n):
	i=1
	array=[1]
	hello = [1]
	prime = []
	while i <= n:
		b = i 
		prime=[]
		while b > 0:
			sol = i % b
			if sol == 0 and i != b:
				array.append(i)
			b -= 1
		i += 1
	i = 0
	ratio = 0 
	while i < len(array):
		if array.count(i) == 1:
			print (i)
		i += 1

print ('This code will output a list of prime numbers until the number you entered.')
a = int(input ('Please enter a number : '))
print ('The list of prime numbers up to this number is :')
prime (a)





 

