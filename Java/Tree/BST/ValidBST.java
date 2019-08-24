/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class ValidBST {
    public boolean isValidBST(TreeNode root) {
        ArrayList<Integer> list = new ArrayList<Integer>();
        if(null == root || (null == root.left && null == root.right) )
            return true;
        list = list = inorder(root, list);
        int len = list.size();
        for(int i = 0 ; i < len - 1 ; i++) {
            if(list.get(i)>=list.get(i+1))
                return false;
        }
        return true;
    }
    
    static ArrayList<Integer> inorder(TreeNode root, ArrayList<Integer> list) {
        if(null!=root.left) list = inorder(root.left, list);
        list.add(root.val);
        if(null!=root.right) list = inorder(root.right, list);
        return list;
    }
}