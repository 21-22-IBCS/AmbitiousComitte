
nums = [10,4,3,9,2,1]
    
for i in range(len(nums)):
    min_index = i
    for j in range (i+1, len(nums)):
        if nums[j] < nums[min_index]:
            min_index = j
    nums[i], nums[min_index] = nums[min_index], nums[i]
    

    print(nums)

