class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        running_max = -1
        for idx in range(len(arr) - 1, -1 ,-1):
            new_max = max(running_max, arr[idx])
            arr[idx] = running_max
            running_max = new_max
        return arr
