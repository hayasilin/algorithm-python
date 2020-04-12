import collections
import unittest

class CompareStrings:
	def __init__(self, str1, str2):
		self.str1 = str1
		self.str2 = str2

	def compare_strings(self):
		if len(self.str1) != len(self.str2):
			return -1

		map1 = collections.Counter(self.str1)
		map2 = collections.Counter(self.str2)

		for key, value in map1.items():
			if key not in map2 or map2[key] != value:
				return -1

		return 0

class ModuleTest(unittest.TestCase):
	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_same_strings(self):
		compare_strings = CompareStrings("abc", "abc")
		self.assertEqual(compare_strings.compare_strings(), 0)
		compare_strings = CompareStrings("aabc", "aabc")
		self.assertEqual(compare_strings.compare_strings(), 0)

	def test_same_strings_permutations(self):
		compare_strings = CompareStrings("abc", "cba")
		self.assertEqual(compare_strings.compare_strings(), 0)
		compare_strings = CompareStrings("aabc", "caba")
		self.assertEqual(compare_strings.compare_strings(), 0)

	def test_different_strings(self):
		compare_strings = CompareStrings("abc", "zxe")
		self.assertEqual(compare_strings.compare_strings(), -1)
		compare_strings = CompareStrings("abc", "aabc")
		self.assertEqual(compare_strings.compare_strings(), -1)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(ModuleTest("test_same_strings"))
    suite.addTest(ModuleTest("test_same_strings_permutations"))
    suite.addTest(ModuleTest("test_different_strings"))

    runner = unittest.TextTestRunner()
    runner.run(suite)
