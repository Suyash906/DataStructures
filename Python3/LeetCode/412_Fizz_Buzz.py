class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for ele in range(1, n+1):
            if ele % 15 == 0:
                res.append('FizzBuzz')
            elif ele % 5 == 0:
                res.append('Buzz')
            elif ele % 3 == 0:
                res.append('Fizz')
            else:
                res.append(str(ele))
        return res