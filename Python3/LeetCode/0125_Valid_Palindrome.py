"""
125. Valid Palindrome
"""
import unittest
def is_valid_char(ch):
	ascii = ord(ch)
	if (ascii >= 65 and ascii <= 90) or (ascii >= 97 and ascii <= 122):
		return True
	return False

def is_valid_palindrome(s):
	if not s: return True
	start = 0
	end = len(s) - 1
	
	while start < end:
		while not is_valid_char(s[start]):
			start += 1
		while not is_valid_char(s[end]):
			end -= 1
		if s[start] != s[end] and s[start] != s[end].lower() and s[end].upper() != s[start]:
			return False
		start += 1
		end  -= 1
	return True



class ValidPalindromeTest(unittest.TestCase):
	def test_is_valid_palindrome(self):
		dataTrue = ["nitin", "ni.   t ** i 000 N", "Ni t. in"]
		dataFalse = ["abcd"]

		for sentence in dataTrue:
			self.assertTrue(is_valid_palindrome(sentence))

		for sentence in dataFalse:
			self.assertFalse(is_valid_palindrome(sentence))


if __name__ == '__main__':
	unittest.main()
