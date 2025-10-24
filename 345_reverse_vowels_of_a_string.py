"""
LeetCode Problem 345: Reverse Vowels of a String
------------------------------------------
Given a string s, reverse only all the vowels in the string
and return the resulting string.

Vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear
in both lowercase and uppercase.

Example:
    Input:  s = "hello"
    Output: "holle"

    Input:  s = "leetcode"
    Output: "leotcede"
------------------------------------------

Explanation of the Problem
------------------------------------------
We are asked to reverse only vowels while keeping
the positions of all other characters the same.

For example:
    s = "MahdiTabesh"
    → vowels are [a, i, a, e]
    → reversed vowels = [e, a, i, a]
    → final output = "MehdaTibash"

------------------------------------------
Approach 1: Two-Pointer Technique (O(n))
------------------------------------------
1. Convert the string to a list (since strings are immutable).
2. Initialize two pointers: left = 0, right = len(s) - 1.
3. Move both pointers toward each other:
   - Increment left until it points to a vowel.
   - Decrement right until it points to a vowel.
4. Swap the two vowels.
5. Continue until left >= right.
6. Join the list back into a string.

This method efficiently performs the swaps in a single pass.
------------------------------------------
Time Complexity:  O(n)
Space Complexity: O(n)  (for list conversion)
------------------------------------------
"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        s = list(s)
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] not in vowels:
                left += 1
                continue
            if s[right] not in vowels:
                right -= 1
                continue

            # Swap vowels
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return ''.join(s)


"""
------------------------------------------
Example Dry Run
------------------------------------------
s = "hello"

Initial: s = ['h', 'e', 'l', 'l', 'o']
vowels = {'a','e','i','o','u','A','E','I','O','U'}

→ left = 0 ('h' not vowel) → left = 1
→ right = 4 ('o' is vowel)
Swap s[1] and s[4] → ['h','o','l','l','e']

Final string = "holle"
------------------------------------------
"""

if __name__ == "__main__":
    sol = Solution()
    print(sol.reverseVowels("hello"))       # Output: "holle"
    print(sol.reverseVowels("leetcode"))    # Output: "leotcede"
    print(sol.reverseVowels("MahdiTabesh")) # Output: "MehdaTibash"
