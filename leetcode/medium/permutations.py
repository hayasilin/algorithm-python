import sys

# Solution 1
def permutations(line, result):
    if len(line) <= 0:
        print(result)
    tmp = result
    for i in range(0, len(line)):
        tmp = result + line[i]
        permutations(line[:i] + line[(i+1):], tmp)

# line = sys.stdin.readline()
# permutations(line, "")
permutations(["a", "b", "c"], "")

# Solution 2
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

# Solution 3
def permute(nums):
        result = []
        dfs(nums, result, [])
        return result
    
def dfs(nums, result, path):
    if not nums:
        result.append(path)
    else:
        for i in range(len(nums)):
            dfs(nums[:i] + nums[i + 1:], result, path + [nums[i]])

print(permute([1,2,3]))