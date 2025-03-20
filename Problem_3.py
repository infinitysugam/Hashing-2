# For every character if it is in set then remove from the set and increase length by 2
# If not then keep in set
# At last if anything is in set then add 1 to length and return it
# Time complexity = O(n)
# Space Complexity = O(1)

class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashset = set()
        length = 0
        for i in s:
            if i in hashset:
                length = length + 2
                hashset.remove(i)
            else:
                hashset.add(i)
        if len(hashset)>0:
            length = length +1
        return length
    
        