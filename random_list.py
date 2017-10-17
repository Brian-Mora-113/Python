from random import randint
def randlist(r,usedlist,done):
	sum = 0
	alpha = [ "A","b","B","c","C","d"]
	usedlist[r] = 1
	c = alpha[r]
	print (len(usedlist))
	
	
	
	for i in range (len(usedlist)):
		sum = sum + usedlist[i]
	print (c,usedlist," sum ",sum)
	if sum == 6:
		done = True
	return c,usedlist,done
    
    
def main():
	# initial variables
	used = [0,0,0,0,0,0]
	done = False #boolean
	######################
	while done == False:
		r = randint(0,5)
		c = randlist(r,used,done)
		if done == True:
			done == True
		#print (used)
		print(c,end="")
            
main()         
 
 
