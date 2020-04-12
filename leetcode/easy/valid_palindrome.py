class Solution:
    def is_palindrome(self, s: str) -> bool:
        filtered_chars = filter(lambda ch: ch.isalnum(), s)
        lowercase_filtered_chars = map(lambda ch: ch.lower(), filtered_chars)

        filtered_chars_list = list(lowercase_filtered_chars)
        reversed_chars_list = filtered_chars_list[::-1]

        return filtered_chars_list == reversed_chars_list

    def is_palindrome_using_two_pointers(self, s: str) -> bool:
        i, j = 0, len(s) - 1

        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1

            if i < j and s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True

import unittest

class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def tearDown(self):
        pass

    def test_is_palindrome(self):
        self.assertTrue(self.solution.is_palindrome("A man, a plan, a canal: Panama"))
        self.assertFalse(self.solution.is_palindrome("race a car"))

        self.assertTrue(self.solution.is_palindrome_using_two_pointers("A man, a plan, a canal: Panama"))
        self.assertFalse(self.solution.is_palindrome_using_two_pointers("race a car"))

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(SolutionTest("test_is_palindrome"))

    runner = unittest.TextTestRunner()
    runner.run(suite)