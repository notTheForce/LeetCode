def getConcatenation(nums: list[int]) -> list[int]:
    ans=[]*2*len(nums)
    ans=nums+nums
    return ans

arr=[1,2]
print(getConcatenation(arr))

