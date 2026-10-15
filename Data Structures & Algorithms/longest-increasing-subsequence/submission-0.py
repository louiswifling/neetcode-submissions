

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        n = len(nums)

        distinct_nums = list(set(nums))
        m = len(distinct_nums)

        distinct_sorted_indices = sorted(range(m), key = lambda i: distinct_nums[i])

        rank_map = {distinct_nums[distinct_sorted_indices[i]]: i for i in range(m)}

        ranks = [rank_map[num] for num in nums ]
          

        DP = [0] * m

        print(ranks)

        for i in range(n): 
            

            max_le_ending = max([DP[j] for j in range(ranks[i]) ] + [0])


            DP[ranks[i]] = max(DP[ranks[i]], max_le_ending + 1)
        


        print(DP)
        return max(DP)
