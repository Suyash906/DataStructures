class IsSubsequenceLC {
    public boolean isSubsequence(String s, String t) {
        int sl = s.length();
        int tl = t.length();
        int i=0,j=0;
        while(i<sl&&j<tl){
            if(s.charAt(i) == t.charAt(j))
                i++;
            j++;
        }
        if(sl == i)
            return true;
        else
            return false;
    }
}