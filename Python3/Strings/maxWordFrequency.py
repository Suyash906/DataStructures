def stringPreProcess(literatureText):
	literatureText = literatureText.replace("'", " ")
	literatureText = literatureText.replace(',', ' ')
	literatureText = literatureText.replace('.', '')
	return literatureText

def maxFrequency(literatureText, wordsToExclude):
	literatureText = stringPreProcess(literatureText)
	
	literatureTextList = literatureText.split(' ')
	
	literatureTextList = [i for i in literatureTextList if i not in wordsToExclude]

	literatureTextList = [i.lower() for i in literatureTextList]

	countMap = {}
	maxCount = 0
	maxFrequencyWordList = []
	for element in literatureTextList:
		if element in countMap:
			countMap[element] += 1
		else:
			countMap[element] = 1
		if countMap[element] > maxCount:
			maxCount = countMap[element]

	for key, value in countMap.items():
		if maxCount == value:
			maxFrequencyWordList.append(key)

	return maxFrequencyWordList

if __name__=='__main__':
	literatureText = 'Jack and Jill went to the market to buy bread and cheese. Cheese is Jack\'s and Jill\'s favorite food'
	wordsToExclude = ['and', 'he', 'the', 'to', 'is', 'Jack', 'Jill']
	print(maxFrequency(literatureText, wordsToExclude))