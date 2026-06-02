class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        curr_max = -1
        answer = [0] * len(arr)
        for idx in range(len(arr) - 1, -1, -1):
            answer[idx] = curr_max
            curr_max = max(arr[idx], curr_max)
        
        return answer