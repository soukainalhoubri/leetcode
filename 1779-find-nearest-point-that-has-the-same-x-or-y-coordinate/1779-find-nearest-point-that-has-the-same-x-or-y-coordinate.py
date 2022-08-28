class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        manhattan=float(inf)
        answer=-1
        for index,point in enumerate(points):
            if point[0]==x or point[1]==y:
                if (abs(point[0]-x)+abs(point[1]-y))<manhattan or manhattan==float(inf):
                    answer=index
                    manhattan=abs(point[0]-x)+abs(point[1]-y)
        return answer
                    