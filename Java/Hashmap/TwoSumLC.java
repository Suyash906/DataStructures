class TwoSumLC {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> map = new HashMap<Integer,Integer>(); 
        int len = nums.length;
        int first=0,second=0,diff;
        for(int i=0;i<len;i++){
            diff = target-nums[i];
            if(map.containsKey(nums[i])){
                second = i;
                first = map.get(nums[i]);
                break;
            } else{
                map.put(diff,i);   
            }
        }
        int[] res = new int[2];
        res[0] = first;
        res[1] = second;
        return res;
    }
}