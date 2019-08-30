class RotatedDigit {
    public int rotatedDigits(int N) {
        int c=0;
        for(int i=1;i<=N;i++){
            if(isValid(i)&&isGood(i,lengthN(i))){
                c++;
            }    
        }
        return c;
    }
    
    static int lengthN(int N){
        int c = 0;
        while(N!=0){
            c++;
            N=N/10;
        }
        return c;
    }
    
    static boolean isValid(int N){
        int dig;
        while(N!=0){
            dig=N%10;
            if(3 == dig || 4 == dig || 7 == dig)
                return false;
            N=N/10;
        }
        return true;
    }
    
    static boolean isGood(int N, int len){
        HashMap<Integer,Integer> map = new HashMap<Integer,Integer>();
        map.put(2,5);
        map.put(5,2);
        map.put(6,9);
        map.put(9,6);
        map.put(1,1);
        map.put(0,0);
        map.put(8,8);
        int num =0, i=0 ;
        int temp = N, dig;
        while(N!=0){
            dig=N / ( (int)Math.pow(10,len) );
            if(dig != map.get(dig)) return true;
            N = N - (dig * ((int)Math.pow(10,len--)));
        }
        return false;
    }
}