def getRow(rowIndex):
        dp = []
        for i in range(0,rowIndex+1):
            if i == 0:
                dp.append([1])
            else:
                templ=[]
                l2 = [0] + dp[-1] + [0]
                for j in range(len(dp[-1])+1):
                    templ.append(l2[j]+l2[j+1])
                dp.append(templ)
        return dp[-1]