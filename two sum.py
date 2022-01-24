def twoSum(nums, target):
    dictn = dict()
        
    for i in range(len(nums)):
       num=nums[i]
       j = target-num
                
       if num in dictn:
           return [dictn[num], i]
                   
       else:
           dictn[j] = i
                
print(twoSum([2,7,11,15], 9))


