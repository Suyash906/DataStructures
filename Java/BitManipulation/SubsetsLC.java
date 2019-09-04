class SubsetsLC {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        List<Integer> temp = null;
        int len = nums.length;
        long setLen = (long)Math.pow(2,len);
        int c,i;
        for(c=0;c<setLen;c++){
            temp = new ArrayList<Integer>();
            for(i=0;i<len;i++){
                if( (c & (1<<i)) > 0)
                    temp.add(nums[i]);
            }
            res.add(temp);
            temp=null;
        }
        return res;
    }
}