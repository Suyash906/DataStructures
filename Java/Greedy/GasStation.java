class GasStation {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int len = gas.length;
        if(1 == len) {
            return gas[0]-cost[0] >=0 ? 0 : -1;
        }
            
        int start = 0;
        int end  = 1;
        int curr = gas[start] - cost[start];
        while( curr<0 || start!=end) {
            while(start!=end && curr<0) {
                curr = curr - (gas[start]-cost[start]);
                start = (start+1)%len;
                if(0 == start)
                    return -1;
            }
            curr = curr + (gas[end] - cost[end]);
            end = (end + 1) % len;
        }
        return start;
    }
}