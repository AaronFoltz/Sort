def BubbleSort(list):
	# Length of the list
	n = len(list)
	
	swapped = True
	
	# While swapped, keep looping
	while(swapped):
		swapped = False
		
		# Loop through each element in the list
		for i in range(0,n-1):
			
			if(list[i] > list[i+1]):
				# Swap the value
				temp = list[i]
				list[i] = list[i+1]
				list[i+1] = temp
				swapped = True
		# Optimized BubbleSort
		n = n-1
	print list

BubbleSort([5,1,4,2,8,5,1,4,2,8])
