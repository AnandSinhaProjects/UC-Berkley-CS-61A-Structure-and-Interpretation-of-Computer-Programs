def isSubsequence(s: str, t: str):
        if len(s)>len(t):
            return False
        else:
            s = list(s)
            t = list(t)
            temp = []
            for i in range(len(s)):
                if s[i] in t:
                    temp.append(t.index(s[i]))
                    t.remove(t[temp[-1]])
                else:
                    return False
            if sorted(temp) == temp:
                return True
            else:
                return False