def knapsack_01(weights, values, total_weight):
    rows = len(weights)+1
    cols = total_weight+1
    
    dp = [[0 for _ in range(cols)] for _ in range(rows)]
    
    for i in range(1,rows):
        for j in range(1,cols):
            
            if j < weights[i - 1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], values[i-1] + dp[i-1][j-weights[i-1]])
    return dp[len(weights)][total_weight]
    
def knapsack_01_recursive(weights, values, index, total_weight, total_value):
    if index == len(weights):
        return total_value
    
    if weights[index] > total_weight:
        return knapsack_01_recursive(weights, values, index+1, total_weight, total_value)
    
    # case 0
    case_0 = knapsack_01_recursive(weights, values, index+1, total_weight, total_value)
    # case 1
    case_1 = knapsack_01_recursive(weights, values, index+1, total_weight-weights[index], total_value+values[index])
    
    return max(case_0, case_1)
    
if __name__ == '__main__':
    total_weight = 7
    weights = [1, 3, 4, 5]
    values = [1, 4, 5, 7]
    expected = 9
    assert expected == knapsack_01(weights, values, total_weight)
    assert expected == knapsack_01_recursive(weights, values, 0, total_weight, 0)
    total_weight = 8
    weights = [2, 2, 4, 5]
    values = [2, 4, 6, 9]
    expected = 13
    assert expected == knapsack_01(weights, values, total_weight)
    assert expected == knapsack_01_recursive(weights, values, 0, total_weight, 0)
    
    total_weight = 8
    weights = [1, 5, 2, 6]
    values = [20, 20, 30, 50]
    expected = 80
    assert expected == knapsack_01(weights, values, total_weight)
    assert expected == knapsack_01_recursive(weights, values, 0, total_weight, 0)
    
    total_weight = 10
    weights = [20,10,10]
    values = [30,20,40]
    expected = 40
    assert expected == knapsack_01(weights, values, total_weight)
    assert expected == knapsack_01_recursive(weights, values, 0, total_weight, 0)
    
    total_weight = 456
    weights = [48, 72, 30, 52, 80, 58, 92, 55, 85, 50, 35, 60, 82, 64, 88, 37, 99, 94, 91, 39, 42, 97, 45, 47, 69, 61, 57, 40, 41, 86, 77, 54, 98, 87, 63, 70, 76, 93, 67, 46, 43, 59, 73, 71, 62, 51, 33, 89, 38, 49]
    values = [166, 114, 159,154, 94, 191, 105, 64, 23, 42, 18, 129, 185, 133, 171, 134, 168, 16, 68, 11, 80, 150, 62, 47, 182, 142, 93, 112, 137, 33, 153, 11, 99, 180, 176, 49, 105, 152, 180, 124, 160, 29, 62, 197, 28, 45, 37, 119, 32, 147]
    expected = 1506
    assert expected == knapsack_01(weights, values, total_weight)
    # assert expected == knapsack_01_recursive(weights, values, 0, total_weight, 0) TLE!!!!!
