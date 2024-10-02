#
# @lc app=leetcode id=9 lang=python
#
# [9] Palindrome Number
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, x):
        stringx=str(x)
        if(stringx==(stringx[::-1])):
            return True
        else:
            return False
        
# @lc code=end

