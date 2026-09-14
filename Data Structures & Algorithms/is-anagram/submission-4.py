class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        f1 = {}
        f2 = {}
        for letter in s:
            f1[letter] = f1.get(letter,0) + 1
        for letter in t:
            f2[letter] = f2.get(letter,0) + 1
        if len(f1) != len(f2):
            return False
        for letter in f1.keys():
            if letter not in f2 or f1[letter] != f2[letter]:
                return False
        return True

        
            
        
        