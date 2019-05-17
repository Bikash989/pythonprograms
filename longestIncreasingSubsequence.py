# complexity: o(n^2)
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
    try:
        list = [] #empty list
        n = int(input("Enter n?\n"))
        print("Enter {} numbers".format(n))
        i = 0
        while i < n:
            list.append(int(input()))
            i += 1
        # a = [7,11,-5,-2,15,1,16,6,7,11,8,9,0]
        lis = LongestIncreasingSubsequence(list)
        print("\nLongest Increasing Subsequence: {}".format(lis.get()))
    except ValueError as e:
        print("\nValueError: Expecting Integers Only\n\nSystem Message :: {}".format(e))
    except Exception as e:
        print("Error: {}".format(e))


if __name__ == "__main__": main()
