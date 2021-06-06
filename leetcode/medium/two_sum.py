class Solution:
	def two_sum_fast(self, nums: [int], target: int) -> [int]:
	        map = {}
	        for i, num in enumerate(nums):
	            if target - num in map:
	                return [map[target-num], i]
	            
	            map[num] = i


	def two_sum_slow(self, nums: [int], target: int) -> [int]:
	        map = {}
	        for i in range(len(nums)):
	            if target - nums[i] in map:
	                return [map[target-nums[i]], i]
	            
	            map[nums[i]] = i

import unittest

class SolutionTest(unittest.TestCase):
	def setUp(self):
		self.solution = Solution()

	def tearDown(self):
		pass

	def test_two_sum_fast(self):
		expected = [0, 1]
		result = self.solution.two_sum_fast([2, 7, 8, 9], 9)
		self.assertEqual(result, result)

	def test_two_sum_slow(self):
		expected = [0, 1]
		result = self.solution.two_sum_slow([2, 7, 8, 9], 9)
		self.assertEqual(result, result)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(SolutionTest("test_two_sum_fast"))
    suite.addTest(SolutionTest("test_two_sum_slow"))

    runner = unittest.TextTestRunner()
    runner.run(suite)
