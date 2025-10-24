"""
LeetCode Problem 209: Minimum Size Subarray Sum
-----------------------------------------------
Given an array of positive integers `nums` and a positive integer `target`,
return the minimal length of a contiguous subarray
of which the sum is greater than or equal to `target`.
If there is no such subarray, return 0.

Example:
    Input:  target = 7, nums = [2,3,1,2,4,3]
    Output: 2
    Explanation: The subarray [4,3] has the smallest length under the problem constraint.

-----------------------------------------------
Explanation of the Problem
-----------------------------------------------
We need the *smallest contiguous subarray* whose sum >= target.

Since all numbers are positive, we can use the **sliding window technique**:
- Expand the right boundary to increase the sum
- Shrink the left boundary while the sum >= target
- Keep track of the minimum window size found

This ensures O(n) time complexity because both pointers
(left and right) move through the array at most once.
"""

class SlidingWindowSolution:
    def minSubArrayLen(self, target, nums):
        left = 0
        curr_sum = 0
        min_len = float('inf')

        for right in range(len(nums)):
            curr_sum += nums[right]

            # Shrink window while sum >= target
            while curr_sum >= target:
                min_len = min(min_len, right - left + 1)
                curr_sum -= nums[left]
                left += 1

        return 0 if min_len == float('inf') else min_len


"""
-----------------------------------------------
Example Dry Run
-----------------------------------------------
target = 7, nums = [2,3,1,2,4,3]

Step-by-step:
    right=0 → curr_sum=2  (<7)
    right=1 → curr_sum=5  (<7)
    right=2 → curr_sum=6  (<7)
    right=3 → curr_sum=8  (>=7)
        → update min_len=4
        → shrink: curr_sum=6
    right=4 → curr_sum=10 (>=7)
        → update min_len=4
        → shrink: curr_sum=7 (>=7)
        → update min_len=3
        → shrink: curr_sum=4
    right=5 → curr_sum=7  (>=7)
        → update min_len=2 

Final Answer: 2
-----------------------------------------------
Time Complexity:  O(n)
Space Complexity: O(1)
-----------------------------------------------
"""

if __name__ == "__main__":
    # Example test
    nums = [2, 3, 1, 2, 4, 3]
    target = 7

    solver = SlidingWindowSolution()
    print("Minimum Subarray Length:", solver.minSubArrayLen(target, nums))
