"""

Link - https://www.geeksforgeeks.org/find-starting-indices-substrings-string-s-made-concatenating-words-listl/


"""
def findSubStringIndices(s, L):
	word_size = len(L[0])

	word_count = len(L)

	size_L = word_size * word_count

	res = []
	
	if len(s) < size_L:
		return res

	word_map = dict()

	for word in L:
		word_map[word] = word_map.get(word, 0) + 1
	
	for i in range(0, len(s) - size_L + 1, 1):
		temp_word_map = word_map.copy()

		j = i
		count = len(temp_word_map)
		while j < i+size_L:

			word = s[j:j+word_size]

			if word not in word_map or temp_word_map[word] ==0:
				break

			temp_word_map[word]-=1
			j+=word_size
			count-=1
		
		if 0 == count:
			res.append(i)
	
	return res


def main(): 
	s = "barfoothefoobarman"
	L = ["foo", "bar"] 
	indices = findSubStringIndices(s, L) 
	
	print(indices)

if __name__ == '__main__':
	main()