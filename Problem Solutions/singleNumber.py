
def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

# Example usage
nums = [2,2,1]
single = singleNumber(nums)
print(f"The single number is: {single}")


