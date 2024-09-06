import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        match = re.match(p,s)
        if match.group()==s:
            return True
        else:
            return False