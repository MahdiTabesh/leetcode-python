"""
LeetCode Problem 917: Reverse Only Letters
------------------------------------------
Given a string `s`, reverse only the English letters in the string and return
the resulting string. All non-letter characters (digits, punctuation, etc.)
must remain in their original positions.

Examples:
    Input:  "ab-cd"
    Output: "dc-ba"

    Input:  "a-bC-dEf-ghIj"
    Output: "j-Ih-gfE-dCba"

------------------------------------------
Explanation of the Problem
------------------------------------------
We are asked to reverse the relative order of only the alphabetic characters
('a'..'z', 'A'..'Z'), while leaving all other characters where they are.
This means the *indices* of non-letters do not change, but letters should
appear in the reversed order they had in the original string.

------------------------------------------
Approach 1 (Two Pointers) — O(n) time, O(1) extra space
------------------------------------------
This is the optimal and most common technique for in-place reordering tasks.

Idea:
    - Convert the string to a list (strings are immutable in Python).
    - Maintain two indices:
        left  → start of the list
        right → end of the list
    - While left < right:
        * If s[left] is NOT a letter:  move left  forward
        * Else if s[right] is NOT a letter: move right backward
        * Else both are letters: swap them, move both pointers inward

Why this works:
    - Non-letter characters are skipped over (so they never move).
    - Every valid letter on the left eventually swaps with the next valid
      letter from the right, which produces the reversed order for letters.

------------------------------------------
Approach 2 (Stack / List of Letters) — O(n) time, O(n) space
------------------------------------------
    - First pass: collect all letters in a list.
    - Second pass: rebuild the string; when you see a letter, pop from the
      collected list (which gives you letters in reverse order).
This is simpler conceptually but uses extra memory.

------------------------------------------
Dry Run (Two Pointers) on "a-bC-dEf-ghIj"
------------------------------------------
s = list("a-bC-dEf-ghIj")
left = 0, right = 12 (0-indexed)
- s[left]='a' (letter), s[right]='j' (letter)  → swap → 'j-...-...Ia'
- Move inward: left=1, right=11
- s[1]='-' (not letter) → left=2
- s[2]='b'(L), s[11]='I'(L) → swap
- Repeat until left >= right

Final result: "j-Ih-gfE-dCba"

------------------------------------------
Correctness & Edge Cases
------------------------------------------
- Empty string: returns empty string.
- Only non-letters: unchanged (e.g., "123-+=" → "123-+=").
- Only letters: fully reversed (e.g., "abc" → "cba").
- Mixed cases preserved (uppercase/lowercase remain as-is).
- Unicode letters: Python's str.isalpha() returns True for many alphabets,
  but LeetCode tests for this problem are about English letters; isalpha()
  still behaves correctly for those.

------------------------------------------
Time & Space Complexity
------------------------------------------
Two-pointer method:
    Time:  O(n) — each index moves at most n steps total
    Space: O(1) extra — in-place within the character list

Stack method:
    Time:  O(n)
    Space: O(n)

------------------------------------------
"""

from typing import List


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        """
        Reverse only the letters in `s`, keeping non-letters fixed in place.

        Args:
            s (str): Input string possibly containing letters and non-letters.

        Returns:
            str: String where letters are reversed and non-letters unchanged.
        """
        chars = list(s)          # Work on a mutable list
        left, right = 0, len(chars) - 1

        while left < right:
            if not chars[left].isalpha():
                left += 1
            elif not chars[right].isalpha():
                right -= 1
            else:
                # Safe simultaneous swap in Python
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1

        return "".join(chars)


# ------------------------------------------
# Optional Alternative: Stack-based solution
# ------------------------------------------
class StackSolution:
    def reverseOnlyLetters(self, s: str) -> str:
        letters = [c for c in s if c.isalpha()]  # collect letters
        out = []
        for c in s:
            if c.isalpha():
                out.append(letters.pop())       # pop from end => reversed
            else:
                out.append(c)
        return "".join(out)


if __name__ == "__main__":
    # Quick sanity checks (matches LeetCode examples)
    tests = [
        ("ab-cd", "dc-ba"),
        ("a-bC-dEf-ghIj", "j-Ih-gfE-dCba"),
        ("Test1ng-Leet=code-Q!", "Qedo1ct-eeLg=ntse-T!"),
        ("", ""),
        ("123-+=", "123-+="),
        ("ABC", "CBA"),
    ]

    sol = Solution()
    alt = StackSolution()

    print("Two-Pointer Results:")
    for s, expected in tests:
        got = sol.reverseOnlyLetters(s)
        print(f"  Input: {s:25s}  Output: {got:25s}  OK? {got == expected}")

    print("\nStack-Based Results:")
    for s, expected in tests:
        got = alt.reverseOnlyLetters(s)
        print(f"  Input: {s:25s}  Output: {got:25s}  OK? {got == expected}")
