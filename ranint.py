# save file as ranint.py
from random import randint
def rint():
	r = randint(65,90)
	if (r==64):
		r = 42
	return r
	
def main():
	for i in range (10000):
		z = rint()
		print (z,end=" ")
	
main()
