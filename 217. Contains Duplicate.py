class Solution:
    # """Brute force solution O(n^2), fails with really long lists"""
    # def containsDuplicate(self, nums: List[int]) -> bool:
    #     for num, i in enumerate(nums):
    #         if i in nums[num+1:]:
    #             # print(f'{i} exists in {nums[num+1:]}')
    #             return True
    #     return False
        
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False
            