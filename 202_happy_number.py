"""
LeetCode Problem 202: Happy Number
----------------------------------
Write an algorithm to determine if a number n is a happy number.

A happy number is defined by the following process:
1. Starting with any positive integer, replace the number by the sum of the squares of its digits.
2. Repeat the process until the number equals 1 (which means it's a happy number),
   or it loops endlessly in a cycle that does not include 1.
3. Return True if n is a happy number, and False otherwise.

Example:
    Input: n = 19
    Output: True
    Explanation:
        1² + 9² = 82
        8² + 2² = 68
        6² + 8² = 100
        1² + 0² + 0² = 1  → Happy!

------------------------------------------
Intuition
------------------------------------------
We keep replacing the number with the sum of squares of its digits.
If we ever reach 1 → it's a happy number.
If we start seeing the same number again → we are in a loop (not happy).

To detect loops, we use a **set** to remember numbers we’ve already seen.

------------------------------------------
Helper Function
------------------------------------------
We’ll create a small helper `get_next(n)` that returns
the sum of squares of digits of `n`.
"""

class HappyNumber:
    def get_next(self, n: int) -> int:
        """Return the sum of the squares of digits of n."""
        total = 0
        while n > 0:
            digit = n % 10
            total += digit * digit
            n //= 10
        return total


"""
------------------------------------------
Approach 1: Using a Set (Cycle Detection)
------------------------------------------
Algorithm:
1. Initialize an empty set `seen` to track visited numbers.
2. While n is not 1 and not in `seen`:
   - Add n to `seen`
   - Replace n with the sum of squares of its digits (using get_next)
3. If n == 1 → return True
   Otherwise → False (loop detected)

Time Complexity:  O(log n)
Space Complexity: O(log n)
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = sum(int(digit) ** 2 for digit in str(n))
        return n == 1


"""
------------------------------------------
Example Dry Run
------------------------------------------
Example: n = 19

Step 1: 1² + 9² = 82
Step 2: 8² + 2² = 68
Step 3: 6² + 8² = 100
Step 4: 1² + 0² + 0² = 1

We reached 1 → Happy Number 

------------------------------------------
Example: n = 2
2² = 4 → 16 → 37 → 58 → 89 → 145 → 42 → 20 → 4 (loops)
→ Not Happy 
------------------------------------------
Time Complexity:  O(log n)
Space Complexity: O(log n)
------------------------------------------
"""

if __name__ == "__main__":
    # Test cases
    happy = Solution()
    print("Input: 19 →", happy.isHappy(19))  # True
    print("Input: 2  →", happy.isHappy(2))   # False
