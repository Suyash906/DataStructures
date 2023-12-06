// 1239. Maximum Length of a Concatenated String with Unique Characters

class Solution {
	private boolean hasUniqueCharSet(String word) {
		if (word == null || word.length() == 0) return true;

		boolean[] charSet = new boolean[26];

		for(int i = 0; i< word.length(); i++) {
			int asciiValue = (int)(word.charAt(i)) - 97;
			if (charSet[asciiValue]) return false;
			charSet[asciiValue] = true;
		}
		return true;
	}
    public int maxLength(List<String> arr) {
    	if (arr == null || arr.length() == 0) return 0;

    	List<String> res = new ArrayList<>();
    	res.add("");
    	int best = 0;

    	for (String word: arr) {
    		for(int i =0; i< res.size(); i++) {
    			String newWord = res.get(i) + word;
    			if (hasUniqueCharSet(newWord)) {
    				best = Math.max(best, newWord.length);
    			}
    		}
    	}

    	return best;
    }
}