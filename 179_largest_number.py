"""
LeetCode Problem 179: Largest Number
------------------------------------------
Given a list of non-negative integers nums, arrange them such that
they form the largest possible number and return it as a string.

Example:
    Input: nums = [3, 30, 34, 5, 9]
    Output: "9534330"

------------------------------------------
Problem Understanding
------------------------------------------
We want to arrange numbers so that when concatenated together, 
they form the largest possible number. This isn’t normal numeric sorting —
it depends on how the numbers combine as strings.

For example:
    '9' + '34' = '934'
    '34' + '9' = '349'
Since '934' > '349', '9' should come *before* '34'.

That’s the entire idea behind the custom comparison.
"""

# ---------------------------------------------------
# Approach 1: Using cmp_to_key (Traditional way)
# ---------------------------------------------------
# In this approach, we define a custom comparison function
# that takes two elements (x and y) and decides their order
# based on x+y and y+x.
#
# For example:
#     compare('9', '34') -> '934' > '349' → return -1 (keep x before y)
#
# The cmp_to_key function converts our compare() function
# into a form Python’s sort() can understand.
# ---------------------------------------------------

from functools import cmp_to_key
from typing import List

class SolutionWithCompare:
    def largestNumber(self, nums: List[int]) -> str:
        # Step 1: Convert all numbers to strings
        nums = list(map(str, nums))

        # Step 2: Define custom compare function
        def compare(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0

        # Step 3: Sort using custom rule
        nums.sort(key=cmp_to_key(compare))

        # Step 4: Join all elements into one string
        result = ''.join(nums)

        # Step 5: Handle case like [0, 0] → "0"
        return '0' if result[0] == '0' else result


"""
------------------------------------------
Why compare returns -1, 1, 0 ?
------------------------------------------
In sorting:
    - return -1 → x comes before y
    - return 1  → y comes before x
    - return 0  → they are equal

Example:
    x = '9', y = '34'
    x+y = '934', y+x = '349'
    '934' > '349' → x first → return -1
------------------------------------------
"""

# ---------------------------------------------------
# Approach 2: Using lambda key function (Simpler way)
# ---------------------------------------------------
# This approach avoids cmp_to_key by using a single-line key function.
# We multiply each string by 10 (x*10) to make all comparable strings
# of equal “length” pattern.
#
# Example:
#   '3'  → '3333333333'
#   '30' → '3030303030'
#   '34' → '3434343434'
#   '5'  → '5555555555'
#   '9'  → '9999999999'
#
# Then Python’s normal lexicographic sorting works correctly.
# ---------------------------------------------------

class SolutionWithLambda:
    def largestNumber(self, nums: List[int]) -> str:
        # Step 1: Convert to string
        nums = list(map(str, nums))

        # Step 2: Sort using key=lambda x: x*10
        # lambda x: x*10 → repeats each string 10 times to normalize comparison
        nums.sort(key=lambda x: x * 10, reverse=True)

        # Step 3: Join into one string
        result = ''.join(nums)

        # Step 4: Handle leading zero case
        return '0' if result[0] == '0' else result


"""
------------------------------------------
Why 'x*10' ?
------------------------------------------
If we directly sort strings, Python compares alphabetically:
    '9' > '5' > '3' (fine)
But for '30' and '3':
    '30' < '3' because '3' == '3' but the shorter one ('3') ends first.

So we artificially repeat each string 10 times, 
ensuring fair comparison like:
    '34'*10 = '3434343434'
    '30'*10 = '3030303030'
    '3'*10  = '3333333333'

Now they have a consistent pattern for sorting.
------------------------------------------
String comparison in Python:
------------------------------------------
Python compares character by character (like dictionary order):
    '9' > '5' because '9' comes after '5'
    '34' > '30' because '3' == '3' but '4' > '0'
    '30' > '3' because longer string wins if prefix is same.
------------------------------------------
"""

# ---------------------------------------------------
# Comparing both approaches
# ---------------------------------------------------
# Efficiency
#   cmp_to_key  → more string concatenations → slower
#   lambda x*10 → simpler and faster (good enough for LeetCode)
#
# Correctness
#   Both are correct for inputs ≤ 10^9
#
# Readability
#   lambda version is shorter, cleaner, and easier to understand.
# ---------------------------------------------------

if __name__ == "__main__":
    nums = [3, 30, 34, 5, 9]
    sol1 = SolutionWithCompare()
    sol2 = SolutionWithLambda()

    print("Using cmp_to_key(compare):", sol1.largestNumber(nums))
    print("Using lambda x*10:", sol2.largestNumber(nums))
