from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        #first of all, we should list the edges:
        color={i:-1 for i in range(len(graph))}
        n=len(graph)
        visited=set()
        for i in range(n):
            if color[i]==-1:
                color[i]=1
            q=deque()
            q.append(i)
            visited=set()
            while q:
                current=q.popleft()
                visited.add(current)
                for adj in graph[current]:
                    if color[adj]==-1:
                        color[adj]=1-color[current]
                    elif color[adj]==color[current]:
                        return False
                    if adj not in visited:
                        q.append(adj)
            if len(visited)==n:
                return True
        return True
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         color={i:-1 for i in range(len(graph))}
#         color[0]=1
#         n=len(graph)
#         q=deque()
#         q.append(0)
#         visited=set()
#         while q:
#             current=q.popleft()
#             print("current =",current)
#             visited.add(current)
#             count=0
#             for adj in graph[current]:
#                 print("adj of",current,"=",adj)
#                 if color[adj]!=-1 and color[current]==color[adj]:
#                     print("got into first if")
#                     return False
#                 elif color[adj]==-1 :
#                     print("color[adj]=",color[adj])
#                     print("got into second if")
#                     color[adj]=1-color[current]
                    
#                 if adj not in visited:
#                     q.append(adj)
#                     count+=1
#             if count==0 and not q and len(visited)!=n:
#                 return False
                
                    
#             print(color)
            
#         return True

    
#     #testing:
    


    
# neighbors=[0,2]
# while loop:
#     current=1
#     q=[2,3]
#     visited=(0,1)
#     neighbors loop:
#         color={0:1,1:0,2:0,3:0}