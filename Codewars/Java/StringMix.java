import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.*;
public class Mixing {
    
    public static String mix(String s1, String s2) {
      // your code
      String finalResult = "";
      Map<Character,Integer> s1_map = new HashMap<Character,Integer>();
      Map<Character,Integer> s2_map = new HashMap<Character,Integer>();
      
      HashSet<Character> charSet = new HashSet<Character>();
      
      Map<Character,Integer> combined_map = new HashMap<Character,Integer>();
      Map<Character,Integer> source = new HashMap<Character,Integer>();
      
      int len1 = s1.length();
      int len2 = s2.length();
      
      for(int i=0;i<len1;i++){
        char curr = s1.charAt(i);
        if(isLowerCase(curr)){
          if(s1_map.containsKey(curr)){
            s1_map.put(curr, s1_map.get(curr)+1);
          } else {
            s1_map.put(curr, 1);
            charSet.add(curr);
          }
        }
      }
      //System.out.println(s1_map);
      for(int i=0;i<len2;i++){
        char curr = s2.charAt(i);
        if(isLowerCase(curr)){
          if(s2_map.containsKey(curr)){
            s2_map.put(curr, s2_map.get(curr)+1);
          } else {
            s2_map.put(curr, 1);
            charSet.add(curr);
          }
        }
      }
      
      Iterator<Character> iC = charSet.iterator();
      while(iC.hasNext()){
    	char curr = iC.next();
    	
    	if(!s1_map.containsKey(curr) && true == s2_map.containsKey(curr)){
    		combined_map.put(curr, s2_map.get(curr));
    		source.put(curr, 2);
    		continue;
    	} else if(!s2_map.containsKey(curr)  && s1_map.containsKey(curr)){
    		combined_map.put(curr, s1_map.get(curr));
    		source.put(curr, 1);
    		continue;
    	}
        int val1 = s1_map.get(curr);
        int val2 = s2_map.get(curr);
        if(1 == val1 && 1 == val2)
        	continue;
        else{
        	if(val1>val2){
        		combined_map.put(curr, val1);
                source.put(curr,1);
        	} else if(val2>val1){
        		combined_map.put(curr, val2);
            	source.put(curr,2);
          } else{
        	  	combined_map.put(curr, val2);
        	  	source.put(curr,0);
          }
        }  
      }
      
      LinkedHashMap<Character, Integer> reverseSortedMap = new LinkedHashMap<>();
      
      combined_map.entrySet()
      .stream()
      .sorted(Map.Entry.comparingByValue(Comparator.reverseOrder())) 
      .forEachOrdered(x -> reverseSortedMap.put(x.getKey(), x.getValue()));
      
      
      finalResult = combineString(reverseSortedMap,source);
      //System.out.println(reverseSortedMap);
      return finalResult;
      
    }
    
    public static boolean isLowerCase(char ch){
      if(ch >= 'a' && ch <= 'z')
        return true;
      return false;
    }
    
    public static String combineString(LinkedHashMap<Character, Integer> reverseSortedMap, Map<Character,Integer>source){
    	String finalString = "";
    	Map<Integer,List<String>> sortedCharMap = new HashMap<Integer,List<String>>();
    	for (Map.Entry<Character, Integer> entry : reverseSortedMap.entrySet()) {
    	    char key = entry.getKey();
    	    int value = entry.getValue();
    	    if(value>1){
    	    	String  currentString = "";
        	    currentString = currentString + (source.get(key)==0 ? "=:" :  source.get(key)+":");
        	    for(int i =0 ;i<value;i++){
        	    	currentString = currentString + key;
        	    }
        	    if(sortedCharMap.containsKey(value)){
        	    	List<String> currentList = sortedCharMap.get(value);
        	    	currentList.add(currentString);
        	    	sortedCharMap.put(value, currentList.stream().sorted().collect(Collectors.toList()));
        	    } else {
        	    	List<String> currentList = new ArrayList<String>();
        	    	currentList.add(currentString);
        	    	sortedCharMap.put(value, currentList);
        	    }
    	    }
    	    
    	}
    	LinkedHashMap<Integer,List<String>> keySortedMap = new LinkedHashMap<>();
        
    	sortedCharMap.entrySet()
        .stream()
        .sorted(Map.Entry.comparingByKey(Comparator.reverseOrder())) 
        .forEachOrdered(x -> keySortedMap.put(x.getKey(), x.getValue()));
    	
    	for (Map.Entry<Integer,List<String>> entry : keySortedMap.entrySet()) {
    	    List<String> value = entry.getValue();
    	    for(int i = 0;i<value.size();i++){
    	    	finalString = finalString + value.get(i) + "/";
    	    }
    	}
    	int len = finalString.length();
    	return 0 == len ? finalString : finalString.substring(0, finalString.length()-1);
    }
    
    public static void main(String[] args){
//    	String res1 = mix("A aaaa bb c", "& aaa bbb c d");
//    	System.out.println(res1);
    	
    	//String res2 = mix("mmmmm m nnnnn y&friend&Paul has heavy hats! &", "& aaa bbb c dmy frie n d Joh n has ma n y ma n y frie n ds n&");
    	//System.out.println(res2);
    	
//    	String res3 = mix("mmmmm m nnnnn y&friend&Paul has heavy hats! &", "my frie n d Joh n has ma n y ma n y frie n ds n&");
//    	System.out.println(res3);
    	
    	String res1 = mix("Are they here", "yes, they are here");
    	System.out.println(res1);
    	
    	String res2 = mix("looping is fun but dangerous", "less dangerous than coding");
    	System.out.println(res2);
    	
    	String res3 = mix(" In many languages", " there's a pair of functions");
    	System.out.println(res3);
    	
    	String res4 = mix("Lords of the Fallen", "gamekult");
    	System.out.println(res4);
    	
    	
    	String res5 = mix("codewars", "codewars");
    	System.out.println(res5);
    	
    	String res6 = mix("A generation must confront the looming ", "codewarrs");
    	System.out.println(res6);
    	
    }
}
