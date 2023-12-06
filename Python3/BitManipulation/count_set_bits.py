import unittest

def count_set_bits(number):
	count = 0
	while number:
		remainder = number % 2
		if remainder == 1:
			count += 1
		number = number // 2
	return count

def count_set_bits_bitwise(number):
	count = 0
	while number:
		count += (number & 1)
		number >>= 1

	return count 


class CountBitTest(unittest.TestCase):
	def test_count_bit_set(self):
		self.assertEqual(6, count_set_bits(125))

	def test_count_bit_set_biwise(self):
		self.assertEqual(6, count_set_bits_bitwise(125))


def main():
	unittest.main()

if __name__ == '__main__':
	main()
	