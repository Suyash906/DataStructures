import unittest
from collections import defaultdict
def check_permutation_sorting(s1, s2):
	if not s1 and not s2: return True
	if not s1 or not s2 or len(s1) != len(s2): return False
	
	s1, s2 = sorted(s1), sorted(s2)
	
	for i in range(len(s1)):
		if s1[i] != s2[i]:
			return False
	return True

def check_permutation_map(s1, s2):
	if not s1 and not s2: return True
	if not s1 or not s2 or len(s1) != len(s2): return False

	char_map = defaultdict(int)
	for char in s1:
		char_map[char] += 1
	
	for char in s2:
		char_map[char] -= 1

	for char, count in char_map.items():
		if count != 0: return False
	
	return True




class CheckPermutationTest(unittest.TestCase):
	dataTrue = [("abcd", "dcba"), ("", "")]
	dataFalse = [("aabcd", "abcd"), ("", "66"), ("333", "")]

	def test_check_permutation_sorting(self):
		for s1, s2 in self.dataTrue:
			self.assertTrue(check_permutation_sorting(s1, s2))

		for s1, s2 in self.dataFalse:
			self.assertFalse(check_permutation_sorting(s1, s2))

	def test_check_permutation_map(self):
		for s1, s2 in self.dataTrue:
			self.assertTrue(check_permutation_map(s1, s2))

		for s1, s2 in self.dataFalse:
			self.assertFalse(check_permutation_map(s1, s2))




if __name__ == '__main__':
	unittest.main()