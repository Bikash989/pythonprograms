def is_part_of_series(lst):
    '''
     :param:    lst - input is the set of integers (list)
     :output:   returns true if the list is a part of the series defined by the following. 
                f(0) = 0 f(1) = 1 f(n) = 2*f(n-1) - 2*f(n-2) for all n > 1.
    '''
    assert(len(lst) > 0)
    
    if(lst[0] != 0):
        return False
    else:
        if(len(lst) == 1):
            return True
    
    if(lst[1] != 1):
        return False
    else:
        if(len(lst) == 2):
            return True           
  
    a = 0       # first initial value is 0 
    b = 1       # second initial value is 1
    i = 2       # loop variable starting at 2, because we already checked for index 0 and 1
    lst_length = len(lst)
    while(i < lst_length):
        c = 2 * (b - a)        # f(n) = 2 * (f(n-1) - f(n-2)) = 2 * (b - a)     
        if(c != lst[i]):
            return False
        a = b   
        b = c
        
        i += 1    
    
    return True


if __name__ == "__main__":
    print("Enter the list of integers seperated by a Space")
    lst = [int(x) for x in input().split()]
    if(is_part_of_series(lst)):
        print("True: {}. List is PART of the Given Series".format(lst))
    else:
        print("False: {}. List is NOT PART of the Given Series".format(lst))