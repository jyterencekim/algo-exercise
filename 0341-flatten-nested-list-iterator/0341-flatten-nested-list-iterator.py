# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

from dataclasses import dataclass


@dataclass
class Item:
    stack: List
    ptr: int
        
class NestedIterator:
    
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = [Item(nestedList, 0)]
    
    def next(self) -> int:
        self.maintain()
        curr = self.stack[-1]
        ptr = curr.ptr
        curr.ptr += 1
        return curr.stack[ptr].getInteger()
        
    def hasNext(self) -> bool:
        self.maintain()
        return len(self.stack) > 0
        
    def maintain(self) -> None:
        while self.stack:
            curr = self.stack[-1]
            
            if len(curr.stack) == curr.ptr:
                self.stack.pop()
                continue
            
            if curr.stack[curr.ptr].isInteger():
                break
            
            anew = curr.stack[curr.ptr].getList()
            curr.ptr += 1
            self.stack.append(Item(anew, 0))
            
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())