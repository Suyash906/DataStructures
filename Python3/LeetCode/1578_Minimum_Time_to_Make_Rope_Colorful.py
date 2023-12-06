class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
    	if not colors or len(colors) < 2:
    		return 0


    	start, end = 0
    	res = 0
    	while start < len(colors):
    		total_cost = neededTime[start]
    		max_cost = neededTime[start]
    		end = start + 1
    		while end < len(colors) and colors[start] == colors[end]:
    			total_cost += neededTime[end]
    			max_cost += max(max_cost, neededTime[end])
    			end += 1

    		res += (total_cost - max_cost)
    		start = end

    	return res