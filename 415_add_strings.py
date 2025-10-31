"""
LeetCode Problem 415: Add Strings
------------------------------------------
Given two non-negative integers num1 and num2 represented as strings,
return the sum of num1 and num2 as a string.

Constraints:
- You must not use any built-in big integer library (like BigInteger).
- You must not directly convert the inputs to integers (no int(), etc.).

Example 1:
    Input:  num1 = "11",  num2 = "123"
    Output: "134"

Example 2:
    Input:  num1 = "456", num2 = "77"
    Output: "533"

Example 3:
    Input:  num1 = "0",   num2 = "0"
    Output: "0"
"""

# ---------------------------------------------------
# Problem Understanding
# ---------------------------------------------------
# We are basically re-implementing addition by hand — the way you would
# do it on paper:
#   1. Start from the last digit of both strings.
#   2. Add them (plus any carry from the previous step).
#   3. Record the last digit of the sum and carry over the rest.
#   4. Move one step left in both strings until all digits and carry are done.
#
# We’ll build the result in reverse order and finally reverse it at the end.
# ---------------------------------------------------

from typing import List

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # Initialize pointers at the end of both strings
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        result = []

        # Continue while there are digits in either string or a carry remains
        while i >= 0 or j >= 0 or carry:
            # Get current digits (or 0 if pointer is out of range)
            x = ord(num1[i]) - ord('0') if i >= 0 else 0
            y = ord(num2[j]) - ord('0') if j >= 0 else 0

            # Calculate sum and carry
            total = x + y + carry
            result.append(str(total % 10))
            carry = total // 10

            # Move to next digits
            i -= 1
            j -= 1

        # Reverse because we added digits from right to left
        return ''.join(result[::-1])


"""
------------------------------------------
Key Concepts Explained
------------------------------------------
Why use ord(char) - ord('0') ?
   - Converts a single character (e.g. '5') into its numeric value (5).
   - Because we cannot use int(char) directly in this problem.

Why build the result in reverse?
   - We add digits from the rightmost side first (units, tens, ...).
   - So we append each new digit to the end of the list,
     and reverse at the end to get the correct order.

What happens with carry?
   - If the sum of two digits (and previous carry) ≥ 10,
     we keep only the last digit and carry = sum // 10 for next step.

Example Walkthrough:
--------------------
num1 = "456", num2 = "77"

Step-by-step:
   i = 2, j = 1 → 6 + 7 + 0 = 13 → append '3', carry = 1
   i = 1, j = 0 → 5 + 7 + 1 = 13 → append '3', carry = 1
   i = 0, j = -1 → 4 + 0 + 1 = 5 → append '5'
   Reverse result → "533"
------------------------------------------
Time Complexity:  O(max(len(num1), len(num2)))
Space Complexity: O(max(len(num1), len(num2)))
------------------------------------------
"""

if __name__ == "__main__":
    sol = Solution()
    print(sol.addStrings("11", "123"))   # Expected: "134"
    print(sol.addStrings("456", "77"))   # Expected: "533"
    print(sol.addStrings("0", "0"))      # Expected: "0"
