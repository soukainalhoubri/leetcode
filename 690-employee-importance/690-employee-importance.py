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
        visited=set()
        q=deque()
        q.append
        
        #we first need to store the items in a way to make access to them easier by ID
        #we will use a dictionnary
        
        importance={i.id:[i.importance,i.subordinates] for i in employees}
        visited=set()
        visitable=set()
        visitable.add(id)
        q=deque()
        q.append(id)
        answer=0
        while q:
            current=q.popleft()
            visited.add(current)
            for sub in importance[current][1]:
                if current in visitable:
                    visitable.add(sub)
                if sub not in visited:
                    q.append(sub)
        for i in visitable:
            answer+=importance[i][0]
        return answer
            