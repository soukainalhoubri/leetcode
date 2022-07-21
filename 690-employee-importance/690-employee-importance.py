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
        visited=set()#O(V) 
        visitable=set()#O(V) 
        visitable.add(id)
        q=deque()#O(V) 
        q.append(id)
        answer=0#O(1) 
        while q:
            current=q.popleft()
            answer+=importance[current][0]
            for i in importance[current][1]:
                q.append(i)
            
        return answer
        
        
        
        
        # while q: #O(V+E)
        #     current=q.popleft()
        #     visited.add(current)
        #     for sub in importance[current][1]:
        #         if current in visitable:
        #             visitable.add(sub)
        #         if sub not in visited:
        #             q.append(sub)
        # for i in visitable: #O(V)
        #     answer+=importance[i][0]
        # return answer
  





#Time complexity:
#let V = len(employees)= number of vertices & E= number of edges
# T=O(V)+O(V)+O(V+E)

#space complexity:
# S=O(V)



            