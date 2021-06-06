from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        def dfs(root: TreeNode, sum: int, curr: List[int], res: List[List[int]]):
            if not root: return
            curr.append(root.val)
            if not root.left and not root.right and sum == root.val:
                res.append(curr[:])
            else:
                dfs(root.left, sum - root.val, curr, res)
                dfs(root.right, sum - root.val, curr, res)
            curr.pop()
            
        res, curr = [], []
        dfs(root, sum, curr, res)
        return res
        
import unittest

class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def tearDown(self):
        pass

    def test_path_sum(self):
        root = TreeNode(self, 5)
        root.left = TreeNode(self, 4)
        root.right = TreeNode(self, 8)
        root.left.left = TreeNode(self, 11)
        root.left.left.left = TreeNode(self, 7)
        root.left.left.right = TreeNode(self, 2)
        root.right.left = TreeNode(self, 13)
        root.right.right = TreeNode(self, 4)
        root.right.right.left = TreeNode(self, 5)
        root.right.right.right = TreeNode(self, 1)

        expected = [
        [5,4,11,2],
        [5,8,4,5]
        ]
        result = self.solution.pathSum(self, root, 22)
        self.assertEqual(expected, result)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(SolutionTest("test_path_sum"))

    runner = unittest.TextTestRunner()
    runner.run(suite)
