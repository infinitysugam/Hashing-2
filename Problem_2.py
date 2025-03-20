# For each index calculate the running index.
# Store the sum as key in hashmap and store the first time sum index as value
# Handle edge case by adding sum as 0 for index - 1
# Time Complexity : O(n)
# Space Complexity : O(1)

class Solution:
    def findMaxLength(self, nums: List[int]):
        max_length = 0 
        running_sum = 0 
        hashmap = {0:-1}
        for i in range(0,len(nums)):
            if nums[i] == 1:
                running_sum = running_sum + 1
            else:
                running_sum = running_sum - 1

            if running_sum in hashmap.keys():
                temp = i-hashmap[running_sum]
                if temp > max_length:
                    max_length = temp
            else:
                hashmap[running_sum] = i
        return max_length



        