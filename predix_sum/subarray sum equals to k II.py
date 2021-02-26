class Solution:
    """
    @param nums: a list of integer
    @param k: an integer
    @return: return an integer, denote the minimum length of continuous subarrays whose sum equals to k
    """
    def subarraySumEqualsKII(self, nums, k):
        # write your code here
        prefix_sum = self.get_prefix_sum(nums)
        answer = float('inf')
        sum2index = {0:0}  #create a hashmap to store the prefix_sum of current prefix_index
        for end in range(len(nums)):
            if prefix_sum[end + 1] - k in sum2index: #the amount of prefixsum is 1 more than the len(array), there is a 0 before the 0+0 in sum_.Here satisfied there is a subarray = k
                length = end + 1 - sum2index[prefix_sum[end+1]-k] #dont for get length always need to plus 1. 
                answer = min(answer, length)
            sum2index[prefix_sum[end + 1]] = end + 1
        return answer
        
        
    def get_prefix_sum(self, nums): # build a helper() to get the prefix_sum
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)
        return prefix_sum


# Description
# Given an array of integers and an integer k, you need to find the minimum size of continuous subarrays whose sum equals to k, and return its length.
# if there are no such subarray, return -1.
# the integer nums[i] may lower than 0




# Example1:
# Input: nums = [1,1,1,2] and k = 3
# Output: 2



#solution:
    #1). array: 0,  1,  2,  3,  4,  5
       #sum_:0  0,  1,  3,  6,  10,  15
   #process :0,0+0,0+1,1+2,3+3,6+4,10+5

    


    

    



