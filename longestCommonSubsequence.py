#program for Longest Common Subsequence

class LCS:
    def __init__(self, firstString, secondString):
        self._str1 = firstString
        self._str2 = secondString
        self._m = len(firstString)
        self._n = len(secondString)
        self._L = [[None] * (self._n + 1)] * (self._m + 1)       #arr = [[0]*cols]*rows [6][5]

    def getLCS(self):
        for i in range(1,self._m+1):
            for j in range(1,self._n+1):
                # print(self._L[i][j], end=" ")
                if i==0 or j==0:
                    self._L[i][j] = 0
                elif self._str1[i-1] == self._str2[j-1]:
                    self._L[i][j] = 1 + self._L[i-1][j-1]
                else:
                    self._L[i][j] = max(self._L[i-1][j], self._L[i][j-1])

        print(self._L[self._m][self._n])
        return s
        
def main():
    str1 = "ABCDGH"
    str2 = "ADH"
    try:
        lcs = LCS(str1, str2)
        print(lcs.getLCS())
        
    except Exception as e:
        print(e)

if __name__ == "__main__": main()
