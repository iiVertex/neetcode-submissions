class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sf = Counter(s)
        tf = Counter(t)
        for k,v in sf.items():
            if k not in tf.keys():
                return False
            if sf[k] != tf[k]:
                return False
        for k,v in tf.items():
            if tf[k] != sf[k]:
                return False
        return True

        
            
        
        