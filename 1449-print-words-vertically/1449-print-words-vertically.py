class Solution:
    def printVertically(self, s: str) -> List[str]:
        res = []
        words = s.split(" ")
        max_len = max(len(word) for word in words)
       
        for i  in range (max_len):
            ver = ''
            for c in words:
                if i < len(c):
                   ver += c[i]
                     
                else:
                    ver += ' '
            res.append(ver.rstrip())
        return res



        