// 1881. Maximum Value after Insertion
/*
          7            1
-255 ->  -2557       -1255
-524 ->  -5247       -1524
-924 ->  -7924       -9234

7
1

255

*/

class Solution {
    public String maxValue(String n, int x) {
        if (n == null || n.length() == 0) return "" + x;

        boolean isNegative = n.charAt(0) == '-' ? true : false;

        if (isNegative) {
            n = n.substring(1);
        }

        StringBuilder sb = new StringBuilder();

        int i = 0;
				String res = "";
        if (!isNegative) {
            while (i < n.length()) {
                int digit = Integer.parseInt(String.valueOf(n.charAt(i)));
                if (x > digit) {
                    sb.append(x);
                    break;
                }
                sb.append(n.charAt(i));
                i++;
            }

            while (i < n.length()) {
                sb.append(n.charAt(i));
                i++;
            }
						if (sb.length() == n.length()) {
							sb.append(x);
						}
						res = sb.toString();

        } else {
						while (i < n.length()) {
                int digit = Integer.parseInt(String.valueOf(n.charAt(i)));
                if (x < digit) {
                    sb.append(x);
                    break;
                }
                sb.append(n.charAt(i));
                i++;
            }

            while (i < n.length()) {
                sb.append(n.charAt(i));
                i++;
            }
						if (sb.length() == n.length()) {
							sb.append(x);
						}
						res = "-" + sb.toString();

        }
        return res;
    }
}