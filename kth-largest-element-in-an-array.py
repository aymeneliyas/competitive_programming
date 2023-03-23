class Solution:
    def merge_sort(self,left, right,arr):
        
        if left == right:
            return [arr[left]]
        mid = left + (right-left) // 2
        left_half = self.merge_sort(left,mid,arr)
        right_half = self.merge_sort(mid+1,right,arr)

        arr = []
        l = 0
        r = 0
        while l < len(left_half) and r < len(right_half):
            if left_half[l] > right_half[r]:
                arr.append(left_half[l])
                l += 1
            else:
                arr.append(right_half[r])
                r += 1
        
        arr.extend(right_half[r:])
        arr.extend(left_half[l:])
        return arr      

    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr = self.merge_sort(0,len(nums)-1,nums)
        return arr[k-1]