def printmove(fr,to):
	print("Moved from " + str(fr)+" to "+str(to))

def TowerOfHanoi(n,fr,to,spare):
	if n==1:
		printmove(fr,to)
	else:
		TowerOfHanoi(n-1,fr,spare,to)
		TowerOfHanoi(1,fr,to,spare)
		TowerOfHanoi(n-1,spare,to,fr)

TowerOfHanoi(int(input("Enter the number of rings in the source peg\n")),'A','B','C')