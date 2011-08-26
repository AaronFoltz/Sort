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


def SelectionSort(list):
	# Iterate through each element in the array
	for i in range(0, len(list)):
		# The minimum is at this index so far
		min = i;
		for j in range(i+1, len(list)):
			if(list[j] < list[min]): 
				min = j
		
		# Swap the values
		temp = list[i]
		list[i] = list[min]
		list[min] = temp
				
	
	print list	
	
SelectionSort([5,1,4,2,8,5,1,4,2,8])