"""
LeetCode Problem 560: Subarray Sum Equals K
------------------------------------------
Given an array of integers `nums` and an integer `k`,
return the total number of contiguous subarrays whose sum equals to `k`.

Example:
    Input: nums = [1,1,1], k = 2
    Output: 2

------------------------------------------
Explanation of the Problem
------------------------------------------
We need to count all *contiguous* subarrays whose total sum = k.

A subarray is defined by two indices (start and end), and its sum can be found by:
    subarray_sum(i, j) = prefix_sum[j] - prefix_sum[i - 1]

If prefix_sum[j] - prefix_sum[i - 1] = k, then:
    prefix_sum[i - 1] = prefix_sum[j] - k

This leads to an efficient O(n) approach using a HashMap (dictionary)
to store how many times each prefix_sum has occurred.

------------------------------------------
Approach 1: Brute Force (O(n²))
------------------------------------------
Try all possible start and end pairs, calculate each subarray sum.
This is easy to understand but too slow for large inputs (n ≤ 20,000).
"""

class BruteForceSolution:
    def subarraySum(self, nums, k):
        count = 0
        n = len(nums)

        # Loop through all start points
        for i in range(n):
            curr_sum = 0
            # Extend the subarray to every end point
            for j in range(i, n):
                curr_sum += nums[j]
                if curr_sum == k:
                    count += 1
        return count


"""
------------------------------------------
Approach 2: Prefix Sum + HashMap (O(n))
------------------------------------------
We keep track of the running sum (curr_sum) as we go through the array.
We also store how many times each prefix sum has appeared in a dictionary.

For each element:
    - Add it to curr_sum
    - Check if (curr_sum - k) exists in the dictionary:
        If yes, that means there are that many previous prefix sums that
        can form a subarray ending at this index whose total is k.
    - Add curr_sum to the dictionary (incrementing its count).

At the end, 'count' will be our total number of subarrays with sum = k.

------------------------------------------
Why prefix_count.get(curr_sum, 0) + 1 ?
------------------------------------------
If the prefix sum has appeared before, we increase its frequency.
If not, we initialize it with 1 (meaning we've seen it once).
"""

class OptimalSolution:
    def subarraySum(self, nums, k):
        count = 0
        curr_sum = 0
        prefix_count = {0: 1}  # Sum 0 occurs once before we start

        for num in nums:
            curr_sum += num  # running total

            # If curr_sum - k was seen before, those are valid subarrays
            if curr_sum - k in prefix_count:
                count += prefix_count[curr_sum - k]

            # Record this prefix sum
            prefix_count[curr_sum] = prefix_count.get(curr_sum, 0) + 1

        return count


"""
------------------------------------------
Example Dry Run
------------------------------------------
nums = [1, -1, 0], k = 0

Step-by-step:
    prefix_count = {0: 1}
    curr_sum = 0, count = 0

    → num = 1
        curr_sum = 1
        curr_sum - k = 1 → not in prefix_count
        prefix_count = {0:1, 1:1}

    → num = -1
        curr_sum = 0
        curr_sum - k = 0 → found! prefix_count[0] = 1 → count = 1
        prefix_count = {0:2, 1:1}

    → num = 0
        curr_sum = 0
        curr_sum - k = 0 → found! prefix_count[0] = 2 → count += 2
        prefix_count = {0:3, 1:1}

Final count = 3
Valid subarrays: [1, -1], [1, -1, 0], [0]
------------------------------------------
Time Complexity:  O(n)
Space Complexity: O(n)
------------------------------------------
"""

if __name__ == "__main__":
    # Test both approaches
    nums = [1, -1, 0]
    k = 0

    brute = BruteForceSolution()
    optimal = OptimalSolution()

    print("Brute Force Result:", brute.subarraySum(nums, k))
    print("Optimal Result:", optimal.subarraySum(nums, k))
