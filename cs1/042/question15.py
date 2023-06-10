def get_no2(nums):

    #remove
    nums.remove(max(nums))

    return max(nums)

in_list = [8485, 8611, 8848, 8586, 8516]

print(get_no2(in_list))



