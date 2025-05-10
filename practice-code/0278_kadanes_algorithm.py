def Kadanes(nums):
    maxSum = nums[0]
    curSum = 0

    for n in nums:
        curSum = max(curSum, 0)
        curSum += n
        maxSum = max(maxSum, curSum)
    return maxSum



nums = [2, 3, 1, 5, 8, 7, 9]
print(Kadanes(nums))



'''output:

35
'''