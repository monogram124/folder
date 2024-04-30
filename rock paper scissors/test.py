def sortArrayByParity(nums: list[int]) -> list[int]:
    new_arr = []

    for num in nums:
        if num % 2 == 0:
            new_arr[0] = num
            
    return new_arr

print(sortArrayByParity([4,5,7,8,9,4,4]))