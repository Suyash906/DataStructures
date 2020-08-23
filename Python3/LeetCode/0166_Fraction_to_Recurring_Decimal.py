class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:return "0"
        fraction = []
        
        sign = (numerator < 0 ) ^ (denominator < 0)
        
        if sign:
            fraction.append("-")
            
        dividend = abs(numerator)
        divisor = abs(denominator)
        fraction.append(str(dividend//divisor))
        rem =  dividend % divisor
        
        if rem == 0:
            return "".join(fraction)
        
        fraction.append(".")
        rem_map = {}
        
        while rem!=0:
            if rem in rem_map:
                start = rem_map[rem]
                fraction.insert(start, '(')
                fraction.append(')')
                break
            rem_map[rem] = len(fraction)
            rem = rem * 10
            fraction.append(str(rem//divisor))
            rem = rem % divisor
                
        return "".join(fraction)
