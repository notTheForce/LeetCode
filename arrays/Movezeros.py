class Solution:
    def movezeros(self,nums):
       left=0
       for right in range(len(nums)):
           if nums[right]!=0:
               nums[left]=nums[right]
               left+=1

       while left<len(nums):
           nums[left]=0
           left+=1

nums=[0,0,1]
sol= Solution()
sol.movezeros(nums)
print(nums)
