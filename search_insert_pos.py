def searchinsert(nums,target):
    for i in range(len(nums)):
        if nums[i] >= target:
            return i
   
    return len(nums)

print(searchinsert(nums = [1,2,4,5],target = 3)) #return index 2
print(searchinsert(nums = [1,2,3,4,5],target = 3))#return index 2
print(searchinsert(nums = [1,2,3,4,5],target = 7))#return index 5

