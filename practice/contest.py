

class ModList:
    def __init__(self, l):
        self.list = l
    
    def append(self,val):
        self.list.append(val)
            # list[i] = list[i] + val #no item assignment
    
    
    def __add__(self,other):
        sum = [] #empty list
        for a,b in zip(self.list,other.list):
            sum.append(a+b)
        return sum
    # overload __add__ how?
    def __iadd__(self,other):
        for i in range(len(self.list)):
            self.list[i] += other
        return self.list

    def __pos__(self):
        for i in range(len(self.list)):
            self.list[i] += other
        return self.list
        

    def __repr__(self):
        return '{}'.format(self.list)
    
    

a = ModList([1,2,3,4])
b = ModList([10,20])
print(a,b)
c = a+b
print(c)
a.append(20)
b.append(30)
b.append(40)
print(a,b)
print(a+b)
print(a)
a += 2
print(a)