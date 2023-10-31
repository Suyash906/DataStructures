import unittest

def unique_string(word):
	if not word: 
		return True

	char_hash_table = [False for _ in range(256)]

	for char in word:
		char_ascii = ord(char)
		if char_hash_table[char_ascii]:
			return False
		char_hash_table[char_ascii] = True 
	return True  


class UniqueStringTest(unittest.TestCase):

	dataTrue = ['abcd', 'a', '#$(*45g)', 's4fad', '']
	dataFalse = ['23ds2', 'hb 627jh=j ()', 'abcda', 'aaa', '#$(*45g)#']

	def test_unique_string_true(self):
		for word in self.dataTrue:
			self.assertTrue(unique_string(word))

	def test_unique_string_false(self):
		for word in self.dataFalse:
			self.assertFalse(unique_string(word))

if __name__ == '__main__':
	unittest.main()