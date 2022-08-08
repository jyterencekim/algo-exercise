class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        """
        how to keep track of the number/count?
        
        - checking that it is an increasing subseq
        - LIS's may or may not depend on a common previous LIS
          e.g. 1 -3 2 -2 3 -1
        
        - at the end we want to know # of LIS's for [0..L-1]
        - does knowing # of LIS's for the subarray help? probably
          given ans[i][j] ... ans[i][j + 1] = ans[i][j] + 1 if nums[j] < nums[j + 1]?
        
        - checking whether is any newly formable LIS and adding 1 -- our note must carry the length and the counts
        - if we have lis_ending_at[index] containing the lis' length, then we can take max(lis_ending_at) and check how many indices have that max
        """
        
        L = len(nums)
        lis_ending_at = [(1, 1) for _ in range(L)]
        max_lis_len = 1
        
        for j in range(1, L):
            curr_len, curr_count = 1, 1
            for i in range(j):
                left, right = nums[i], nums[j]
                if left < right:
                    prev_len, prev_count = lis_ending_at[i]
                    extended_len = prev_len + 1
                    if extended_len > curr_len:
                        curr_len = extended_len
                        curr_count = prev_count
                    elif extended_len == curr_len:
                        curr_count += prev_count
            max_lis_len = max(max_lis_len, curr_len)
            lis_ending_at[j] = (curr_len, curr_count)
        
        print(lis_ending_at, max_lis_len)
        return sum([lis_ending_at[i][1] for i in range(L) if lis_ending_at[i][0] == max_lis_len])