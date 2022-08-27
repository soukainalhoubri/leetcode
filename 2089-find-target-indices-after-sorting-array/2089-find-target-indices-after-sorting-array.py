class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        answer=[]
        nums.sort()
        for i, val in enumerate(nums):
            if val==target:
                answer.append(i)
        return answer