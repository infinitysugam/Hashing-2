# We do this by running sum approach. For this we calculate the running sum for all array.
# We also calculate the complement. If the complement already exists in hashmap we increase output by 1.
# We keep the running sum and its count in the hashmap
# Time Complexity : O(n)
# Space Complexity : O(n)

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        hashmap = {0:1} #{rsum:count}
        running_sum = 0 
        for i in range(0,len(nums)):
            running_sum = running_sum + nums[i]
            comp = running_sum - k
            if comp in hashmap.keys():
                result = result + hashmap[comp]
            
            if running_sum in hashmap.keys():
                hashmap[running_sum] = hashmap[running_sum] + 1
            else:
                hashmap[running_sum] = 1
        return result
 