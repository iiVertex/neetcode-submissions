class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr = ""

        for char in s.lower():
            if char.isalnum():
                newstr += char

        return newstr == newstr[::-1]
            
