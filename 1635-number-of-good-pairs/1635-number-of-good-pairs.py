class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        # for i in range (len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             count += 1
        # return count
        num_count = {}
        for num in nums:
            if num in num_count:
                count += num_count[num]
                num_count[num] += 1
            else:
                num_count[num] = 1
        return count


        