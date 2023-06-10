def my_median(nums):

    if len(nums) % 2 == 0:

        no1_state = len(nums) // 2 -1

        no1 = nums.pop(no1_state)

        no2 = nums.pop(no1_state)



        return (no1 + no2) / 2
    
    elif len(nums) % 2 !=0:

        no1 = len(nums) // 2

        return nums[no1]
    

print(my_median([1.3, 2.4, 3.5, 4.6, 5.7, 6.8]))
print(my_median([1.3, 2.4, 3.5, 4.6, 5.7]))