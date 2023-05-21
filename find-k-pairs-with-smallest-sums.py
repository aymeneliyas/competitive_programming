class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        ans = []

        arr = [((nums1[0] + nums2[0]), 0, 0)]
        while arr and len(ans) < k:

            tot , i,j  = heapq.heappop(arr)
            if j == 0 and i + 1 < len(nums1):
                heapq.heappush(arr, (nums1[i+1] + nums2[j], i + 1, j))
            if j + 1 < len(nums2):
                heapq.heappush(arr, (nums1[i] + nums2[j+1], i, j + 1))
            
            ans.append([nums1[i], nums2[j]])

        return ans