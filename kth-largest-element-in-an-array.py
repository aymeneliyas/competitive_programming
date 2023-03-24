class Solution:
    def partition(self,l,r,nums):
        pivot = nums[r]
        i = l-1
        
        for j in range(l,r):
            if nums[j] <= pivot:
                i += 1
                nums[i],nums[j] = nums[j],nums[i]
        nums[i + 1], nums[r] = nums[r], nums[i + 1]
        
        return i + 1
    
    def quick_sort(self,l,r,nums):
        if l >= r:
            return

        mid = self.partition(l,r,nums)
        left = self.quick_sort(l,mid-1,nums)
        right = self.quick_sort(mid+1,r,nums)

    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.quick_sort(0,len(nums)-1,nums)
        print(nums)
        return nums[-k]