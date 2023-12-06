// 1615. Maximal Network Rank
import java.util.*;
class Solution {
    public int maximalNetworkRank(int n, int[][] roads) {
        
        Map<Integer, Set<Integer>> neighboursMap = new HashMap<>();

        for(int i = 0; i< roads.length; i++) {
        	int city1 = roads[i][0];
    		int city2 = roads[i][1];
    		if(!neighboursMap.containsKey(city1)) neighboursMap.put(city1, new HashSet<>());
    		if(!neighboursMap.containsKey(city2)) neighboursMap.put(city2, new HashSet<>());
    		neighboursMap.put(city1, neighboursMap.get(city1).add(city2));
    		neighboursMap.put(city2, neighboursMap.get(city2).add(city1));
        }
        int maxCount = 0;
        for( Map.Entry<Integer, Set<Integer>> mapElement : neighboursMap.entrySet()) {
        	int key = mapElement.getKey();
        	Set<Integer> neighbourSet = mapElement.getValue();
        	for(int i: neighbourSet) {
        		maxCount = Math.max(maxCount, neighbourSet.size() + neighboursMap.get(i).size() - 1);
        	}
        }
        return maxCount;
    }
}