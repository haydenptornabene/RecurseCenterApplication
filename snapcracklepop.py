List = range(1,101)

#This line initiates a list with the numbers 1-100(inclusive)


for x in range(len(List)):
	if List[x] % 5 == 0 and List[x] % 3 == 0:
		List[x] = 'CracklePop' 
#This part of the if statement checks elements in list to see if they are divisible by 3 
#and 5. If yes, replace with string 'CracklePop'
	elif List[x] % 3 == 0:
		List[x] = 'Crackle' 
#This part of the if statement checks elements in list to see if they are divisible by 3. 
#If yes, replace with string 'Crackle'
	elif List[x] % 5 == 0:
		List[x] = 'Pop'
#This part of the if statement checks elements in list to see if they are divisible by 5. 
#If yes, replace with string 'Pop'		
	else:
		List[x] = List[x]
#Leave all other elements as is.
		   
print List




