class Solution:
    def validPalindrome(self, s: str) -> bool:

        def isPalindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False

                left += 1
                right -= 1

            return True

        left = 0
        right = len(s) - 1

        while left < right:

            if s[left] != s[right]:

                # Skip the left character
                skip_left = isPalindrome(left + 1, right)

                # Skip the right character
                skip_right = isPalindrome(left, right - 1)

                return skip_left or skip_right

            left += 1
            right -= 1

        return True