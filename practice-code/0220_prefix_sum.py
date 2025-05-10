class PrefixSum:
    
    def __init__(self, nums):
        self.prefix = []
        self.total  = 0
        for n in nums:
            self.total += n
            self.prefix.append(self.total)
            
    # how would you modify this to calcuate post-fix sum
    def rangeSum(self, left, right):
        preRight = self.prefix[right]
        preLeft  = self.prefix[left - 1] if left > 0 else 0
        return (preRight - preLeft)
    

nums = [1, 3, 5, 7, 9]

cls_obj = PrefixSum(nums=nums)
print(cls_obj.rangeSum(0, 4)) # index number of num list



'''output:

25
'''