// you can also use imports, for example:
// import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

class OddOccurrencesInArray {
    public int solution(int[] A) {
        // write your code in Java SE 8
        int len = A.length;
        if(0 == len)
            return 0;
        int pair = A[0];
        
        for(int i = 1;i<len;i++){
            pair = pair ^ A[i];
        }
        return pair;
    }
}