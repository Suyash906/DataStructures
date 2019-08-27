class ContainerWithMostWater {
    public int maxArea(int[] height) {
        int i, j, len, area, s, e, maxarea;
        len = height.length;
        s = 0;
        e = len-1;
        maxarea = 0;
        while(s<e) {
            maxarea = Math.max(maxarea, Math.min(height[e],height[s])*(e-s));
            if(height[s]<height[e])
                s++;
            else
                e--;
        }
        return maxarea;
    }
}