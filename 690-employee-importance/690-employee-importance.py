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
        ids={employee.id:employee for employee in employees}
        importance=0
        q=deque()
        q.append(ids[id])
        while q:
            current=q.popleft()
            importance+=current.importance
            for sub in current.subordinates:
                q.append(ids[sub])
                
        return importance
            