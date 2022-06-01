#Lab #5
#Due Date: 03/22/2020, 11:59PM
########################################
#
# Name: Benjamin Gutierrez
# Collaboration Statement:
#
########################################

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return "Node({})".format(self.value)

    __repr__ = __str__


class Queue:
    '''
        >>> x=Queue()
        >>> x.isEmpty()
        True
        >>> x.dequeue()
        >>> x.enqueue(1)
        >>> x.enqueue(2)
        >>> x.enqueue(3)
        >>> x.enqueue(4)
        >>> print(x)
        Head:Node(1)
        Tail:Node(4)
        Queue:1 2 3 4
        >>> x.isEmpty()
        False
        >>> len(x)
        4
        >>> x.dequeue()
        1
        >>> x.dequeue()
        2
        >>> x.dequeue()
        3
        >>> x.dequeue()
        4
        >>> x.dequeue()
        >>> print(x)
        Head:None
        Tail:None
        Queue:
        >>> x.enqueue(3)
        >>> x.enqueue(2)
        >>> print(x)
        Head:Node(3)
        Tail:Node(2)
        Queue:3 2
        >>> x.dequeue()
        3
        >>> print(x)
        Head:Node(2)
        Tail:Node(2)
        Queue:2
        >>> x.dequeue()
        2
        >>> print(x)
        Head:None
        Tail:None
        Queue:
    '''
    def __init__(self):
        self.head=None
        self.tail=None
        self.count=0

    def __str__(self):
        temp=self.head
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out=' '.join(out)
        return f'Head:{self.head}\nTail:{self.tail}\nQueue:{out}'

    __repr__=__str__

    def isEmpty(self):
        return not self.count


    def enqueue(self, value):
        nn = Node(value)
        # add new node to queue
        if self.isEmpty():
          self.head = nn
        else:
          self.tail.next = nn
        # update tail pointer and counter
        self.tail = nn
        self.count += 1



    def dequeue(self):
        if self.isEmpty():
          return None
        # remove head node
        temp = self.head.value
        if len(self) == 1:
          self.head = None
          self.tail = None
        else:
          self.head = self.head.next
        self.count -= 1
        return temp





    def __len__(self):
        return self.count


