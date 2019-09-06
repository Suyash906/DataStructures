// you can also use imports, for example:
// import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

class MinTrailingZeros {
    public int solution(int[][] A) {
        // write your code in Java SE 8
        int i,j, a, b, min;
        int n = A.length;
        int[][] T = new int[n][n];
        int[][] P = new int[n][n];
        for(i=0;i<n;i++){
            for(j=0;j<n;j++){
                min = Integer.MAX_VALUE;
                if(i == 0 && j ==0 ){
                    min = trailZeros(A[i][j]);     
                }
                T[i][j] = trailZeros(A[i][j]);
                P[i][j] = A[i][j];
                if((i-1)>=0){
                    a = trailZeros(A[i-1][j] * A[i][j]);
                    if(a<min) {
                        min = a;
                        P[i][j] = A[i-1][j] * A[i][j];
                    }
                }
                if((j-1)>=0){
                    b = trailZeros(A[i][j-1] * A[i][j]);
                    if(b<min){
                        min = b;
                        P[i][j] = A[i][j-1] * A[i][j];
                    }
                }
                T[i][j] = min;
                A[i][j] = P[i][j];
            }
        }
        return P[n-1][n-1] == 0 ? 1 :T[n-1][n-1];
    }
    
    static int trailZeros(int x){
        int count=0;
        while(x != 0){
            if(0 == x || x%10 != 0)
                break;
            count++;
            x = x / 10;
        }
        return count;
    }
}