"""
TODO: get the array without duplicates 
  
	: type List[int]
	: rtype int

"""

def removeDuplicates(self, nums):
	
	nums = [1,1,2]	
	if not nums:  # 不存在nums 也就不存在element
		return 0
	count = 0  	#count有多少个不同的value

	for i in range(len(nums)):  	#遍历array里面所有的值
		if nums[count] != nums[i]:
			count += 1				#只有当两个数值不同 count才+1 
			nums[count] = nums[i]   #update nums的值 
	return count +1



"""
TODO: what if the array has not been sorted

"""
