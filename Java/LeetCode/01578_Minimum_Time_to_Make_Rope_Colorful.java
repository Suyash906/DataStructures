// 1578. Minimum Time to Make Rope Colorful

class Solution {
	public int minCost(String colors, int[] neededTime) {
		// null check
		/*
		 a a a  b b b a b b b b
		[3,5,10,7,5,3,5,5,4,8,1]
		 0,1,2 ,3,4,5,6,7,8,9,10


		 a b c
		 1 2 3

		*/
		if (colors == null || colors.length() < 2) return 0;

		int start = 0;
		int end = 1;
		int res = 0;
		while (start < colors.length() && end < colors.length()) {
			int maxCost = neededTime[start]; // 3
			int totalCost = neededTime[start]; // 3
			end = start + 1; // 3
			while (end < colors.length() && colors.charAt(start) == colors.charAt(end)) {
				totalCost += neededTime[end]; // 18
				maxCost = Math.max(totalCost, neededTime[end]); // 8
				end++; // 11
			}
			res += (totalCost - maxCost); // 0
			start = end; // 2
		}
		return res;
	}
}