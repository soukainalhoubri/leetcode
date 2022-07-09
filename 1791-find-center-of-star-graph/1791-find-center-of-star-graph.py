class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        a=edges[0][0]
        if a in edges[1]:
            return a
        else:
            return edges[0][1]