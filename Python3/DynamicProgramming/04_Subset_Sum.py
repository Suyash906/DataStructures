def subset_sum_recursive(nums, total_sum, index, curr_sum):
    if index >= len(nums):
        return False
    if curr_sum == total_sum:
        return True
    if curr_sum > total_sum:
        return subset_sum_recursive(nums, total_sum, index+1, curr_sum)
    case_0 = subset_sum_recursive(nums, total_sum, index+1, curr_sum)
    case_1 = subset_sum_recursive(nums, total_sum, index+1, curr_sum + nums[index])
    
    return case_0 or case_1
    
    
if __name__ == '__main__':
    total_sum = 11
    nums = [2, 3, 7, 8, 10]
    expected = True
    # assert expected == subset_sum_dp(nums, total_sum)
    assert expected == subset_sum_recursive(nums, total_sum, 0, 0)
