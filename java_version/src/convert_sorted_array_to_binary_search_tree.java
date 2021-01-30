
//Definition for a binary tree node.
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode() {

    }

    TreeNode(int val) {
        this.val = val;
    }

    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    int[] nums;

    public TreeNode createTree(int x, int y){
        if (x>y)
            return null;

        int mid = (x+y)/2;
        TreeNode node = new TreeNode(nums[mid]);
        node.left = createTree(x, mid-1);
        node.right = createTree(mid+1, y);
        return node;
    }

    public TreeNode sortedArrayToBST(int[] nums) {
        this.nums = nums;
        return createTree(0, nums.length-1);

    }
}