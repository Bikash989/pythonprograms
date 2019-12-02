class node:
    def __init__(self,data):
        self.value = data
        self.next=None;

class LinkedList:
    def __init__(self):
        self.start = None;
    
    def insert_last(self,value):
        newNode = node(value)
        if(self.start == None):
            self.start = newNode;
        else:
            # search last node to insert
            temp = self.start
            while temp.next != None:
                temp = temp.next
            
            temp.next = newNode


    def delete_first(self):
        if(self.start == None):
            print("Linked List Empty")
        else:
            #temp = self.start
            self.start = self.start.next #if no second present than, start will contain None
    
    def display_list(self):
        if self.start == None:
            print("List empty")
        else:
            temp=self.start
            while(temp != None):
                print(temp.value,end=" ")
                temp = temp.next


if __name__ == '__main__':
    mylist = LinkedList()
    mylist.insert_last(10)
    mylist.insert_last(20)
    mylist.insert_last(30)
    mylist.insert_last(40)
    mylist.display_list()
    print()
    mylist.delete_first()
    mylist.display_list()
