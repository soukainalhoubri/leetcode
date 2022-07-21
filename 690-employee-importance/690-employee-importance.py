"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

from collections import deque

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        #we first need to store the items in a way to make access to them easier by ID
        #we will use a dictionnary: creating an adjaceny list
        
        importance={i.id:[i.importance,i.subordinates] for i in employees}#O(V) T&S
        q=deque()#O(V) 
        q.append(id)
        answer=0#O(1) 
        while q:
            current=q.popleft()
            answer+=importance[current][0]
            for i in importance[current][1]:
                q.append(i)
            
        return answer
        



            