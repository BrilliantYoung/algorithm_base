def misisngNumber(nums):
	'''
	leetcode 268.missing number
    nums is a list
    this type is list[int]
    time complexity:O(logn)
	'''
	nums.sort()
	if nums[-1]!=len(nums):
		return len(nums)
	elif nums[0]!=0:
		return 0
	else:
		for i in range(1,len(nums)):
			temp = nums[i-1]+1
			if nums[i]!=temp:
				return temp

if __name__=='__main__':
	# nums=[3,0,1]
	# nums=[0]
	nums=[1]
	ans = misisngNumber(nums)
	print(ans)