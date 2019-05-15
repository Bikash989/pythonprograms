class LongestIncreasingSubsequence:
    def __init__(self,list):
        self._list = list
        self._L = [None] * len(list)

    def get(self):
        for i in range(0,len(self._list)):
            self._L[i] = 1
            for j in range(0,i):
                if ((self._list[j] < self._list[i]) and (self._L[i] < (1 + self._L[j])) ):
                    self._L[i] = 1 + self._L[j]
        return max(self._L)

def main():
    a = [1,2,3,4,3,10,6,7,11,13]
    lis = LongestIncreasingSubsequence(a)
    print(lis.get())

if __name__ == "__main__": main()
