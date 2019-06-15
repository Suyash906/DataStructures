public class BinarySearch{

     public static void main(String []args){
        int a[] = { 2, 3, 4, 10, 40 };
        int num = 4;
        int result;
        result = binarySearchIterative(a, num);
        System.out.println("binarySearchIterative Result = "+result);
        result = binarySearchRecursive(a, 0, a.length-1, num);
        System.out.println("binarySearchRecursive Result = "+result);
     }
     
     public static int binarySearchIterative(int []a, int num){
        int n = a.length;
        int start = 0;
        int end = n -1;
        int mid;
        while(start<=end){
            mid = (start+end) / 2;
            if(a[mid] == num){
                return (mid+1);
            } else if(a[mid] < num){
                start = mid+1;
            } else {
                end = mid-1;
            }
        }
        return -1; 
     }
     
     public static int binarySearchRecursive(int []a, int start, int end, int num){
         
        if(start <= end){
            int mid = (start+end)/2;
            if(num == a[mid]){
                return (mid+1);
            } else if(a[mid]<num){
                return binarySearchRecursive(a, mid+1, end, num);
            } else{
                return binarySearchRecursive(a, start, mid-1, num);
            }    
        }
        return -1;
     }
}