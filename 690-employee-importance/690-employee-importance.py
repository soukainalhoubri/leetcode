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
    importance=0
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        ids={employee.id:employee for employee in employees}
        self.importance+=ids[id].importance
        def dfs(identifier):
            for sub in ids[identifier].subordinates:
                self.importance+=ids[sub].importance
                dfs(sub)
        dfs(id)
        return self.importance