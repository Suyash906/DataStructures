import unittest
def urlify(url):
	if not url: return ""
	i = 0
	url = [ch for ch in url]
	while i < len(url):
		if url[i] == ' ':
			j = len(url) - 3
			while j >= i + 1:
				url[j+2] = url[j]
				j -= 1
			url[i] = '%'
			url[i+1] = '2'
			url[i+2] = '0'
			i += 3
		else:
			i += 1

	return "".join(url)


def find_actual_length(url):
	i = len(url) - 1
	while url[i] == ' ':
		i -= 1
	return i + 1

def urify_optimized(url):
	"""
	
	"""
	if not url: return ""
	actual_length = find_actual_length(url)

	i = actual_length - 1
	diff = len(url) - actual_length
	while i >= 0:
		if url[i] == ' ':
			url[i-2] = '%'
			url[i-1] = '2'
			url[i] = '0'
		else:
			url[i + diff] = url[i]
		i -= 1

	return url


class URLifyTest(unittest.TestCase):
	data = [('Mr John Smith    ', "Mr%20John%20Smith")]
	
	def urlify_test(self):
		for url, expected_output in self.data:
			self.assertEqual(urlify(url), expected_output)


if __name__ == '__main__':
	url = 'Mr John Smith    '
	print(urlify(url))
	unittest.main()