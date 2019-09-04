class PascalLC {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        if(0 == numRows) {
            return result;
        }
        int size = 1,i;
        List<Integer> currentElement = null;
        while(size!=numRows+1){
            currentElement  = new ArrayList<Integer>();
            for(i = 0; i< size;i++ ){
                if(0 == i || size - 1 == i){
                    currentElement.add(1);
                } else{
                    currentElement.add(result.get(size-2).get(i-1) + result.get(size-2).get(i));
                }
            }
            size++;
            result.add(currentElement);
        }
        return result;
    }
}