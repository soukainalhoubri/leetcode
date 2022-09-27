"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        #I need to clone my node, and I will keep track of its copy to return it.
        def dfs(node,copies):
            for neighbor in node.neighbors:
                if neighbor not in copies:
                    newNode=Node(neighbor.val)
                    copies[neighbor]=newNode
                    # copies[node].neighbors.append(newNode)
                    dfs(neighbor,copies)
                copies[node].neighbors.append(copies[neighbor])
                    
        if not node:
            return None
        newGraph = Node(node.val)
        copies={node:newGraph}
        dfs(node,copies)
        return newGraph
        #for each node, I will make a new copy.
        #I need to populate its neighbors
        #what I wanna make sure of is that, I keep the same created nodes, and create links between them.
        #node1 --> (node2,node3)--> node2-->node1 --> node3-->node1
        
        #to do so, I need to keep trak of the nodes I have already copied, and their copies: hashtable
        
        #example
        
#         (1,[2,4]) (2,[1,3]) (3,[2,4]) (4,[1,3])
        
#         (1',[2',4'])(2',[1',3']) (3',[2',4']) (4',[1',3'])
#         {1:1',2:2'}
         
         #1->(2->1)-->3
         #iterate over its neighbors
         #2 --> not in the dict, so I create a copy for it
         #I add it to current main node's neighbors
         #1--> in dict, so I add it's copy as a neighbor for the current working node : 2
         #3--> not in dict, we create a copy for it, and add to 2' neighs
         # we go through 3neighs
         #2 is in the dict, so we add itscopy to our node's neighs
         #4 not in the dict, create, add, go through 4
         #1 -> in dict, add copy to current neighs
         #3---> in dict, add copy to current neighs
                                             
         
        
        
        
        
        
        