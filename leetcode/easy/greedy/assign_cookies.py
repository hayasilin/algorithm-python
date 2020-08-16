# 先對g, s進行排序先对g, s两个数组进行排序
# 貪心思想1 優先滿足需求因子較小的孩子。因為如果較小需求的孩子無法被滿足，則之後較大的需求更不可能被滿足。
# 貪心思想2 儘量用較小的糖果去優先滿足孩子
def findContentChildren(self, g: List[int], s: List[int]) -> int:
	g.sort()    
	s.sort()
	child  = 0  # 紀錄可以被滿足孩子數
	cookie = 0  # 紀錄可以滿足的糖果數
	while  child <len(g) and cookie < len(s):
		if g[child] <= s[cookie]: 
			child += 1
			cookie += 1

	return child