def findMaximumValueRecursive(weight, value, totalWeight):
    
    return -1

def findMaximumValue(weight, value, totalWeight):
    size = len(weight)
    grid = [[ 0 for col in range(totalWeight+1)] for row in range(size)]
    print(grid)
    return -1

if __name__=='__main__':
    weight = [1,3,4,5]
    value = [1,4,5,7]
    totalWeight  = 7
    print(findMaximumValue(weight, value, totalWeight))