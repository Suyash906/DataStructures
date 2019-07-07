class ClimbingStairsTopDown   {
    public int climbStairs(int n) {
        int memo[] = new int[n+1];
        for(int i = 0 ; i < n+1 ; i++ )
            memo[i] = 0;
        return climb_Stairs(0, n, memo);
    }
    public int climb_Stairs(int i, int n, int[] memo) {
        if (i > n) {
            return 0;
        }
        if (i == n) {
            return 1;
        }
        if(0 == memo[i])
            memo[i] =  climb_Stairs(i + 1, n, memo) + climb_Stairs(i + 2, n, memo);        
        return memo[i];
    }
}