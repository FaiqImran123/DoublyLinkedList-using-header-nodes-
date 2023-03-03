#header node handles boundary cases easily
class Node:
    def __init__(self, val):
        self.data =val
        self.next =None
        self.prev =None
class CircularLinkedList:
    def __init__(self):
        self.head =Node("_")
        self.tail =Node("_")

    def push(self, val):    #append val
        n =Node(val)
        if self.head.next==None:
            self.head.next =n
            n.prev =self.head
            n.next =self.tail
            self.tail.prev =n
        
        else:
            temp =self.tail.prev
            self.tail.prev.next =n
            self.tail.prev =n
            n.prev =temp
            n.next =self.tail
    def pop(self):
        if self.head.next ==None:
            raise Exception("List is empty")
        else:
            t=self.tail.prev.prev
            t.next =self.tail
            self.tail.prev =t
    def remove(self, val):
        c =self.head
        while c!=None:
            if c.data!="_":
                if c.data==val:
                    
                    c.prev.next =c.next
                    c.next.prev =c.prev
                    return
            c =c.next
        raise Exception("Not find a value")
    def add_after(self,v1,v2):   #Insert v1 after v2
        n =Node(v1)
        c =self.head
        while c!=None:
            if c.data!="_":
                if c.data==v2:
                    temp =c.next
                    c.next =n
                    n.prev =c
                    n.next =temp
                    c.next.prev =n
                    return
            c =c.next
        raise Exception("Not found")
    def add_before(self, v1, v2):  #insert v1 before v2
        n =Node(v1)
        c =self.head
        while c!=None:
            if c.data!="_":
                if c.data==v2:
                    temp =c.prev
                    c.prev.next =n
                    n.prev =temp
                    n.next =c
                    c.prev =n
                    return
            c =c.next
        raise Exception("Val Not found")
    def display(self):
        c =self.head
        while c!=None:
   
            if type(c.data)!=str:
                print(c.data, end=" ")
            c =c.next
        print()

def main():
    c =CircularLinkedList()
    c.push(10)
    c.push(20)
    c.push(30)
    c.push(40)
    c.display()
    c.pop()
    c.display()
    c.remove(20)
    c.display()
    c.remove(30)
    c.display()
    c.push(1)
    c.push(20)
    c.push(30)
    c.display()
    c.add_after(0,20)
    c.display()
    c.add_before(9,10)
    c.add_before(23,30)
    c.add_before(77,1)
    c.display()

 




main()