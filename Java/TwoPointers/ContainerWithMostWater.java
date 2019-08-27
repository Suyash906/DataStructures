class ContainerWithMostWater {
    public int maxArea(int[] height) {
        int max = Integer.MIN_VALUE;
        int i, j, len, area;
        len = height.length;
        for(i=0;i<len-1;i++) {
            for(j=i+1;j<len;j++){
                area = min(height[i],height[j]) * (j-i);
                if(area>max)
                    max = area;
            }
        }
        return max;
    }
    static int min(int a, int b) {
        return a > b ? b : a;
    }
}