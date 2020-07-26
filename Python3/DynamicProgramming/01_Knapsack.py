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
    # assert expected == knapsack_01(values, weights, total_weight)
    assert expected == knapsack_01_recursive(weights, values, 0, total_weight, 0)
    print(knapsack_01_recursive(weights, values, 0, total_weight, 0))
    total_weight = 8
    weights = [2, 2, 4, 5]
    values = [2, 4, 6, 9]
    expected = 13
    # assert expected == knapsack_01(values, weights, total_weight)
    assert expected == knapsack_01_recursive(weights, values, 0, total_weight, 0)
    print(knapsack_01_recursive(weights, values, 0, total_weight, 0))
