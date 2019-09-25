class triangle:
    def __init__(self,base=0,height=0,left_side=0,right_side=0):  
        self.base = base
        self.height = height
        self.left_side = left_side
        left_ = 0
        height_ = 0
        right_=0
        if(self.height > 0):
            height_ = self.height / other_triangle.height
        else:
            left_ = self.left_side / other_triangle.left_side
            right_ = self.right_side / other_triangle.right_side
        
        return triangle(base=base_,height=height_,left_side=left_,right_side=right_)
        
    def __ne__(self, other_triangle):
        if(self.height > 0):
            return (self.base != other_triangle.base) or (self.height != other_triangle.height)

        else:
            return ((self.base != other_triangle.base) or (self.left_side != other_triangle.left_side) or (self.right_side != other_triangle.right_side))
        

    def __ge__(self,other_triangle):
        if(self.height > 0):
            return (self.base >= other_triangle.base) or (self.height >= other_triangle.height)

        else:
            return ((self.base >= other_triangle.base) or (self.left_side >= other_triangle.left_side) or (self.right_side >= other_triangle.height))

    def __mul__(self,other_triangle):
        base_ = self.base * other_triangle.base
        left_ = self.left_side * other_triangle.left_side
        right_ = self.right_side * other_triangle.right_side
        height_ = self.height * other_triangle.height
        return triangle(base=base_,height=height_,left_side=left_,right_side=right_)
        


A = triangle(base=20,height=60)
B = triangle(base=30,height=100)

print("Area = {}".format(A.area()))

print("A ({}) not equal B ({}) =  {}  ".format(A,B,(A != B)))   # it's true A not equal B
print("A ({}) greater than B ({}) =  {}  ".format(A,B,(A >= B)))   # it's false A not equal B since A.base is less than B.base


C = A + B       #adding triangle A and B
print("A + B = ({})".format(C))
print()


# demonstration of triangle whose height is not given
print("#####################################################################")

A = triangle(base=2,left_side=5,right_side=6)
B = triangle(base=10,left_side=6,right_side=20)

print("A ({}) not equal B ({}) =  {}  ".format(A,B,(A != B)))
print("A ({}) greater than B ({}) =  {}  ".format(A,B,(A >= B)))  
