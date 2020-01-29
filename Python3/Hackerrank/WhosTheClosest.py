def binarySearch(nums, target):
	start = 0
	end = len(nums) - 1

	while start <= end:
		mid = (start+end)//2

		if nums[mid] == target:
			return mid
		elif nums[mid] < target:
			start = mid + 1
		else:
			end = mid -1
	return -1

def findClosest(s, queries):
	result = []
	if 0 == len(queries):
		return result
	charMap = {}
	for key,char in enumerate(s):
		if char in charMap.keys():
			oldList = charMap[char]
			oldList.append(key)
		else:
			charMap[char] = [key]


	for query in queries:
		char = s[query]
		currList = charMap[char]
		if len(currList) == 1:
			result.append(-1)
			continue

		location = binarySearch(currList, query)
		if -1 == location:
			result.append(-1)
			continue

		leftNeighbour = rightNeighbour = 9999
		if location-1 >= 0:
			leftNeighbour = currList[location-1]

		if location + 1 <= len(currList)-1:
			rightNeighbour = currList[location+1]

		if abs(rightNeighbour - location) < abs(location - leftNeighbour):
			result.append(rightNeighbour)
		else:
			result.append(leftNeighbour)

	return result




s = 'hackerrank'
queries = [4,1,6,8]
result = findClosest(s, queries)

print("result = ", result)