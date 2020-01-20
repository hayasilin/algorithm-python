def permutation(lst):
    if len(lst) == 0:
        return []

    if len(lst) == 1:
        return [lst]

    result = []

    for i in range(len(lst)):
        m = lst[i]
        print("m= ", m)
        remaing_list = lst[:i] + lst[i+1:]
        print("remaing_list = ", remaing_list)
        for p in permutation(remaing_list):
            result.append([m] + p)
            print("result= ", result)

    
    return result

if __name__ == '__main__':
    permutation([1,2,3])



def permute(self, nums):
        result = []
        self.dfs(nums, result, [])
        return result
    
def dfs(self, nums, result, path):
    if not nums:
        result.append(path)
    else:
        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i + 1:], result, path + [nums[i]])