class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current_max=0
        cumulated=0
        for i in range(len(gain)):
            cumulated+=gain[i]
            current_max=max(current_max,cumulated)
        return current_max