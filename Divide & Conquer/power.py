def power(a,b):
	if b==0:
		return 1
	elif b%2 == 0:
		val = power(a,int(b/2))
		return val*val
	else:
		oddval = power(a,b-1)
		return a*oddval

# take base 
a = int(input())
#take exponent
b = int(input())

# to find a^b we divide b in two halves recursively.

answer=power(a,b)
print(answer) 