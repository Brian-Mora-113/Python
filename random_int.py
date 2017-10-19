from random import randint
def randlist(r,usedlist):
	alpha = [ "A","b","B","c","C","d"]
	used = 1
	used[r]
	c = alpha[r]
	#print(usedlist)
	return c
    
    
def main():
	# initial variables
	used = [0,0,0,0,0,0]
	done = False #boolean
	######################
	while done == False:
		r = randint(0,5)
		c = randlist(r,used)
		print (used)
		#print(c,end="")
            
main()         
 
 
