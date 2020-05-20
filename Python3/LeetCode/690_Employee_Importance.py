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
        if len(employees) == 0:
            return 0
        # This map contains Employee id as key and the Employee object as value 
        subordinate_map = {}
        for employee in employees:
            subordinate_map[employee.id] = employee
        
        total_importance = 0
        q = deque([])
        q.append(id)
        while q:
            curr = q.popleft()
            total_importance += subordinate_map[curr].importance
            for subordinate in subordinate_map[curr].subordinates:
                q.append(subordinate)
        return total_importance
