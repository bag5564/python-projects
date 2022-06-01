#LAB 9
#Due Date: 04/11/2020, 11:59PM EST
########################################
#
# Name: Benjamin Gutierrez
# Collaboration Statement:
#
########################################

class MaxPriorityQueue:
    def __init__(self):
        self.heap=[]

    def __str__(self):
        return f'{self.heap}'

    __repr__=__str__

    def __len__(self):
        return len(self.heap)

    def parent(self,index):
        if index <= 1 or index > len(self):
          return None
        i = (index // 2) - 1
        return  self.heap[i]

    def leftChild(self,index):
        if index < 1 or index > len(self):
          return None
        i = 2 * index - 1
        if i >= len(self):
          return None
        return self.heap[i]

    def rightChild(self,index):
        if index < 1 or index > len(self):
          return None
        i = 2 * index
        if i >= len(self):
          return None
        return self.heap[i]

    def insert(self,x):
        self.heap.append(x)
        index = len(self)
        # check if node is in right order
        while index > 1:
          if self.parent(index) < x:
            parentIndex = index // 2
            temp = self.heap[parentIndex - 1]
            self.heap[parentIndex -1] = self.heap[index -1]
            self.heap[index -1] = temp
            index = parentIndex
          else:
            break

    def deleteMax(self):
        if len(self)==0:
            return None
        elif len(self)==1:
            outMax=self.heap[0]
            self.heap=[]
            return outMax

        outMax = self.heap[0]
        # replace the root with the last node
        last = len(self) -1
        self.heap[0] = self.heap[last]
        del self.heap[last]
        # compare new root (index=1) with children nodes and swap it if necessary
        self.repositionNode(1)
        return outMax;

    def repositionNode(self, index):
        leftValue = self.leftChild(index)
        leftIndex = 2 * index
        rightValue = self.rightChild(index)
        rightIndex = 2 * index + 1
        maxValue  = self.heap[index - 1]
        maxIndex = index

        if leftValue != None and leftValue > maxValue:
          maxValue = leftValue
          maxIndex = leftIndex
        if rightValue != None and rightValue > maxValue:
          maxValue = rightValue
          maxIndex = rightIndex

        if maxIndex != index:
          # swap nodes
          temp = self.heap[index - 1]
          self.heap[index -1] = self.heap[maxIndex -1]
          self.heap[maxIndex -1] = temp
          # compare swapped node with children nodes and swap it if necessary
          self.repositionNode(maxIndex)



def heapSort(numList):
    '''
       >>> heapSort([9,7,4,1,2,4,8,7,0,-1])
       [-1, 0, 1, 2, 4, 4, 7, 7, 8, 9]
       >>> heapSort([])
       []
       >>> heapSort(9)
       >>> heapSort([9,'a',4,1,2,4,8,7,0,-1])
    '''
    sortHeap = MaxPriorityQueue()

    if (not isinstance(numList, list)):
      return None
    for item in numList:
      if (not isinstance(item, int) and not isinstance(item, float)):
        return None
      sortHeap.insert(item)
    sortHeap.heap

    sortedList = []
    while len(sortHeap) > 0 :
      node = sortHeap.deleteMax()
      sortedList.insert(0,node)

    return sortedList

