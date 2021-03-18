def sort(nums):
    for i in range(5):
        minpos=i
        for j in range(i,6):
            if nums[j]<nums[minpos]:
                minpos=j
        tmp=nums[i]
        nums[i]=nums[minpos]
        nums[minpos]=tmp


nums=[9,8,7,6,5,4]
sort(nums)
print(nums)