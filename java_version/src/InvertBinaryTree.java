/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode invertTree(TreeNode root) {
        if (root == null){
            return root;
        }
        TreeNode temp = null;
        if (root.right != null){
           temp = root.right;
        }
        root.right = root.left;
        root.left = temp;
        if (root.left != null){
            this.invertTree(root.left);
        }
        if (root.right != null){
            this.invertTree(root.right);
        }
        return root;
    }
}